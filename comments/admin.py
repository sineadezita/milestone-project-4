from django.contrib import admin
from .models import Comment

# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'article', 'created_at', 'is_approved']
    list_filter = ['is_approved']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(is_approved=True)
