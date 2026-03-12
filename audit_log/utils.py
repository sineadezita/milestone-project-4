from .models import AuditLog

def log_action(user, action, detail='', request=None):
    ip_address = None
    if request:
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
        if ip_address:
           ip_address = ip_address.split(',')[0]
        else:
            ip_address = request.META.get('REMOTE_ADDR')

    
    AuditLog.objects.create(
        user=user,
        action=action,
        detail=detail,
        ip_address=ip_address
    )
    