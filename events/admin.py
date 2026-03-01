from django.contrib import admin
from .models import Event

# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'event_date', 'location', 'country', 'is_published']
    list_filter = ['is_published', 'country']
    prepopulated_fields = {'slug': ('title',)}