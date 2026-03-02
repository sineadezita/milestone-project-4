from django.db import models
from django.contrib.auth.models import User
from articles.models import Article

# Create your models here.

class Comment(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name='comments'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments'
    )
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return f'Comment by {self.author} on {self.article}'
