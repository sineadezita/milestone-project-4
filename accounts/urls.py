from django.urls import  path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.profile, name='profile'),
    path('reading-list/', views.reading_list, name='reading_list'),
    path('save-article/<int:article_id>/', views.save_article, name='save_article'),
    path('save-event/<int:event_id>/', views.save_event, name='save_event'),
    path('saved-events/', views.saved_events, name='saved_events'),
]