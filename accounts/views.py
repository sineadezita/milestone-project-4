from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

@login_required
def profile(request):
    """ A view to show the user's profile """
    profile = get_object_or_404(UserProfile, user=request.user)
    context = {
        'profile': profile,
    }
    return render(request, 'accounts/profile.html', context)

@login_required
def reading_list(request):
    """ A view to show the user's saved articles """
    profile = get_object_or_404(UserProfile, user=request.user)
    saved_articles = profile.saved_articles.all()
    context = {
        'saved_articles': saved_articles
    }
    return render(request, 'accounts/reading_list.html', context)

@login_required
def save_article(request, article_id):
    """ Save or unsave an article to the user's reading list """
    from articles.models import Article
    article = get_object_or_404(Article, id=article_id)
    profile = get_object_or_404(UserProfile, user=request.user)

    if article in profile.saved_articles.all():
        profile.saved_articles.remove(article)
        messages.success(request, f'Removed {article.title} from your reading list')
    else:
        profile.saved_articles.add(article)
        messages.success(request, f'Added {article.title} to your reading list')

    return redirect('articles:article_list')

@login_required
def save_event(request, event_id):
    """ Save or unsave and event """
    from events.models import Event
    event = get_object_or_404(Event, id=event_id)
    profile = get_object_or_404(UserProfile, user=request.user)

    if event in profile.saved_events.all():
        profile.saved_events.remove(event)
        messages.success(request, f'Removed {event.title} from your saved events')
    else:
        profile.saved_events.add(event)
        messages.success(request, f'Added {event.title} to your rsaved events')

    return redirect('events:event_list')

@login_required
def saved_events(request):
    """ A view to show the user's saved events """
    profile = get_object_or_404(UserProfile, user=request.user)
    saved_events = profile.saved_events.all()
    context = {
        'saved_events': saved_events,
    }
    return render(request, 'accounts/saved_events.html', context)
