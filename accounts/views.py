from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile

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