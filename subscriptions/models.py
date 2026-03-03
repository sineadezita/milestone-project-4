from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Subscription(models.Model):

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('cancelled', 'Cancelled'),
        ('past_due', 'Past Due')
    ]

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='subscription'
    )
    stripe_customer_id = models.CharField(max_length=250, blank=True)
    stripe_subscription_id = models.CharField(max_length=250, blank=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='cancelled'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} | {self.status}'

