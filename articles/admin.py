from django.contrib import admin
from .models import Category, Article

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'is_premium', 'is_published', 'published_at']
    list_filter = ['is_premium', 'is_published', 'category']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
