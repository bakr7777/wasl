from . import views
from django.urls import path



urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'), 
    path('deals', views.deals, name='deals'), 
    path('reservation', views.reservation, name='reservation'), 
    #path('profile', views.profile, name='profile'), 
    #path('login', views.login, name='login'), 
]