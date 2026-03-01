from django.shortcuts import render, get_object_or_404
from .models import Event

# Create your views here.

def event_list(request):
    """ A view to show all published events """
    events = Event.objects.filter(is_published=True)

    context = {
        'events': events,
    }
    return render(request, 'events/event_list.html', context)

def event_detail(request, slug):
    """ A view to show an individual event """
    event = get_object_or_404(Event, slug=slug, is_published=True)

    context = {
        'event': event,
    }
    return render(request, 'events/event_detail.html', context)
