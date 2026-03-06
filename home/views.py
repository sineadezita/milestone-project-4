from django.shortcuts import render
from articles.models import Article
from events.models import Event

# Create your views here.
def index(request):
    """ A view to return the index page """
    featured_articles = Article.objects.filter(
        is_published='True').order_by('-created_at')[:4]
    upcoming_events = Event.objects.all().order_by('event_date')[:3]

    context = {
        'featured_articles': featured_articles,
        'upcoming_events': upcoming_events,
    }
    return render(request, 'home/index.html', context)
