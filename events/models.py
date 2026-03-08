from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    event_date = models.DateTimeField()
    location = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    website_url = models.URLField(blank=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['event_date']

    def __str__(self):
        return self.title
    
