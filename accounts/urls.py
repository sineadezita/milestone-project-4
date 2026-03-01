from django.urls import  path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.profile, name='profile'),
    path('reading-list/', views.reading_list, name='reading_list'),
]