from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth.models import User
import stripe
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from .models import Subscription
from audit_log.utils import log_action

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.

@login_required
def subscription_page(request):
    """ A view to show the subscription page """
    try:
        subscription = Subscription.objects.get(user=request.user)
    except Subscription.DoesNotExist:
        subscription = None

    context = {
        'subscription': subscription,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
    }
    return render(request, 'subscriptions/subscription_page.html', context)



@login_required
def create_checkout_session(request):
    """ Create a Stripe checkout session """
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price': settings.STRIPE_PRICE_ID,
                'quantity': 1,
            }],
            mode='subscription',
            success_url=request.build_absolute_uri('/subscriptions/success/'),
            cancel_url=request.build_absolute_uri('/subscriptions/cancel'),
            customer_email=request.user.email,
            client_reference_id=request.user.id,
        )
        return redirect(checkout_session.url)
    except Exception as e:
        messages.error(request, f'Something went wrong: {str(e)}')
        return redirect('subscriptions:subscription_page')
    


@login_required
def subscription_success(request):
    """ Manage successful subscriptions """
    log_action(request.user, 'subscribe', 'Subscription created', request)
    messages.success(request, 'Welcome to Atelier Zero One Premium!')
    return render(request, 'subscriptions/success.html')
    



@login_required
def subscription_cancel(request):
    """ Manage cancelled subscription """
    messages.info(request, 'Subscription cancelled.')
    return render(request, 'subscriptions/cancel.html')



@csrf_exempt
def webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    webhook_secret = settings.STRIPE_WEBHOOK_SECRET

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, webhook_secret
        )
    except ValueError:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        user_id = session.get('client_reference_id')
        subscription_id = session.get('subscription')
        customer_id = session.get('customer')

        if user_id:
            try:
                user = User.objects.get(id=user_id)
                Subscription.objects.update_or_create(
                    user=user,
                    defaults={
                        'stripe_customer_id': customer_id,
                        'stripe_subscription_id': subscription_id,
                        'status': 'active'
                    }
                )
                log_action(user, 'subscribe', 'Subscription created', request)
            except User.DoesNotExist:
                pass

    elif event['type'] == 'customer.subscription.deleted':
        subscription_data = event['data']['object']
        customer_id = subscription_data['customer']
        try:
            customer = stripe.Customer.retrieve(customer_id)
            email = customer.get('email')
            if email:
                user = User.objects.filter(email=email).first()
                if user:
                    Subscription.objects.filter(user=user).update(status='cancelled')
                    log_action(user, 'cancel', 'Subscription cancelled via webhook')
        except Exception:
            pass

    return HttpResponse(status=200)
