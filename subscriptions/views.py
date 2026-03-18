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
   try:
       checkout_session = stripe.checkout.Session.create(
           mode='subscription',
           payment_method_types=['card'],
           line_items=[{
               'price': settings.STRIPE_PRICE_ID,
               'quantity': 1,
           }],
           success_url=request.build_absolute_uri('/subscriptions/success/?session_id={CHECKOUT_SESSION_ID}'),
           cancel_url=request.build_absolute_uri('/subscriptions/cancel/'),
           customer_email=request.user.email,
           client_reference_id=str(request.user.id),
       )
       return redirect(checkout_session.url)
   except Exception as e:
       messages.error(request, f'Something went wrong: {str(e)}')
       return redirect('subscriptions:subscription_page')
    


@login_required
def subscription_success(request):
   session_id = request.GET.get('session_id')
   if session_id:
       try:
           session = stripe.checkout.Session.retrieve(session_id)
           Subscription.objects.update_or_create(
               user=request.user,
               defaults={
                   'stripe_customer_id': session.customer or '',
                   'stripe_subscription_id': session.subscription or '',
                   'status': 'active',
               }
           )
           log_action(request.user, 'subscribe', 'Subscription created', request)
       except Exception:
           pass
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
       event = stripe.Webhook.construct_event(payload, sig_header, webhook_secret)
   except ValueError:
       return HttpResponse(status=400)
   except stripe.error.SignatureVerificationError:
       return HttpResponse(status=400)

   event_type = event['type']
   obj = event['data']['object']

   if event_type == 'checkout.session.completed':
       user_id = obj.get('client_reference_id')
       subscription_id = obj.get('subscription')
       customer_id = obj.get('customer')
       email = obj.get('customer_email')

       user = None

       if user_id:
           user = User.objects.filter(id=user_id).first()

       if not user and email:
           user = User.objects.filter(email=email).first()

       if user:
           Subscription.objects.update_or_create(
               user=user,
               defaults={
                   'stripe_customer_id': customer_id or '',
                   'stripe_subscription_id': subscription_id or '',
                   'status': 'active',
               }
           )
           log_action(user, 'subscribe', 'Subscription created', request)

   elif event_type == 'invoice.paid':
       customer_id = obj.get('customer')
       subscription_id = obj.get('subscription')

       sub = (
           Subscription.objects.filter(stripe_customer_id=customer_id).first()
           or Subscription.objects.filter(stripe_subscription_id=subscription_id).first()
       )

       if sub:
           sub.status = 'active'
           sub.save()

   elif event_type == 'customer.subscription.deleted':
       subscription_id = obj.get('id')
       customer_id = obj.get('customer')

       Subscription.objects.filter(
           stripe_subscription_id=subscription_id
       ).update(status='cancelled')

       Subscription.objects.filter(
           stripe_customer_id=customer_id
       ).update(status='cancelled')

   return HttpResponse(status=200)
