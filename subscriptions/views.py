import stripe
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from .models import Subscription

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
        )
        return redirect(checkout_session.url)
    except Exception as e:
        messages.error(request, f'Soemthing went wrong: {str(e)}')
        return redirect('subscriptions:subscription_page')
    


@login_required
def subscription_success(request):
    """ Manage successful subscriptions """
    messages.success(request, 'Welcome to Atelier Zero One Premium!')
    return render(request, 'subscriptions/success.html')



@login_required
def subscription_cancel(request):
    """ Manage cancelled subscription """
    messages.info(request, 'Subscrpition cancelled.')
    return render(request, 'subscriptions/cancel.html')
