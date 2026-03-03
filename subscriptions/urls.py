from django.urls import path
from . import views

app_name = 'subscriptions'

urlpatterns = [
    path('', views.subscription_page, name='subscription_page'),
    path('checkout/', views.create_checkout_session, name='checkout'),
    path('success/', views.subscription_success, name='success'),
    path('cancel/', views.subscription_cancel, name='cancel'),
    path('webhook/', views.webhook, name='webhook'),
]