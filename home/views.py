from django.shortcuts import render
from articles.models import Article
from events.models import Event
from subscriptions.models import Subscription


def index(request):
    """A view to return the index page"""
    featured_articles = Article.objects.filter(
       is_published=True
    ).order_by('-created_at')[:3]
    latest_articles = Article.objects.filter(
       is_published=True
    ).order_by('-updated_at')[:5]
    upcoming_events = Event.objects.all().order_by('event_date')[:3]

    subscription = None
    if request.user.is_authenticated:
        try:
            subscription = request.user.subscription
        except Exception:
            subscription = None

    context = {
       'featured_articles': featured_articles,
       'latest_articles': latest_articles,
       'upcoming_events': upcoming_events,
       'subscription': subscription,
    }
    return render(request, 'home/index.html', context)


def about(request):
    """A view to return the about page"""
    return render(request, 'home/about.html')
