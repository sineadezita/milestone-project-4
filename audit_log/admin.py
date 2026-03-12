from django.contrib import admin
from .models import AuditLog

# Register your models here.

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'action', 'detail', 'ip_address', 'timestamp']
    list_filter = ['action', 'timestamp']
    search_fields = ['user__username', 'detail']
    readonly_fields = ['user', 'action', 'detail', 'ip_address', 'timestamp']
