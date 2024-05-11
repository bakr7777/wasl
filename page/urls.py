from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'), 
    path('deals', views.deals, name='deals'), 
    path('reservation', views.reservation, name='reservation'), 
    path('vir', views.vir, name='vir'), 
    path('addpost', views.addpost, name='addpost'),
    path('update', views.update, name='update'),
    path('condations', views.condations, name='condations'),
    path('ownpro', views.ownpro, name='ownpro'),
    path('project', views.project, name='project'),
    path('prodesc', views.prodesc, name='prodesc'),
    path('twsl', views.twsl, name='twsl'),
    path('<int:id>', views.edit, name='edit'),
    path('favorite', views.favorite, name='favorite'),


    
]
