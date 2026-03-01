from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('events/', views.event_list, name='event_list'),
    path('events/<slug:slug>/', views.event_detail, name='event_detail'),
]