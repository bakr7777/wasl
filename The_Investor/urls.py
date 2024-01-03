from . import views
from django.urls import path



urlpatterns = [
    path('', views.index, name='index'),
    path('browse', views.browse, name='browse'), 
    path('details', views.details, name='details'), 
    path('streams', views.streams, name='streams'), 
    path('profile', views.profile, name='profile'), 
]