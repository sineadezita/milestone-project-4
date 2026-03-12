from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AuditLog(models.Model):
    ACTION_CHOICES = [
        ('login', 'User Login'),
        ('logout', 'User Logout'),
        ('subscribe', 'Subscription Created'),
        ('cancel', 'Subscription Cancelled'),
        ('save_article', 'Article Saved'),
        ('save_event', 'Event Saved'),
        ('comment', 'Comment Posted'),
        ('view_premium', 'Premium Article Viewed'),
    ]

    user = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='audit_logs'
    )
    action = models.CharField(max_length=50, choices=ACTION_CHOICES)
    detail = models.CharField(max_length=200, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']
    
    def __str__(self):
        return f"{self.user} - {self.action} - {self.timestamp:%d %b %Y %H:%M}"
