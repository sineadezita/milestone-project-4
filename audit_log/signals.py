from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from .models import AuditLog

@receiver(user_logged_in)
def login(sender, request, user, **kwargs):
    ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
    if ip_address:
        ip_address = ip_address.split(',')[0]
    else:
        ip_address = request.META.get('REMOTE_ADDR')

    
    AuditLog.objects.create(
        user=user,
        action='login',
        detail='User logged in',
        ip_address=ip_address
    )


@receiver(user_logged_out)
def log_logout(sender, request, user, **kwargs):
    ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
    if ip_address:
        ip_address = ip_address.split(',')[0]
    else:
        ip_address = request.META.get('REMOTE_ADDR')

    AuditLog.objects.create(
        user=user,
        action='logout',
        detail='User ;ogged out',
        ip_address=ip_address
    )
