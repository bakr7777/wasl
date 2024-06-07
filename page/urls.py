from . import views
from django.urls import path
from .views import feasibility_study, confirmation_page
from page.views import feasibility_study
from .views import services
from .views import chat_list, send_message



urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'), 
    path('deals', views.deals, name='deals'), 
    path('reservation', views.reservation, name='reservation'), 
    path('vir', views.vir, name='vir'), 
    path('addpost', views.addpost, name='addpost'),
    
    path('condations', views.condations, name='condations'),
    path('ownpro', views.ownpro, name='ownpro'),
    path('project', views.project, name='project'),
    path('prodesc', views.prodesc, name='prodesc'),
    path('twsl', views.twsl, name='twsl'),
    #path('update_messages/', views.update_messages, name='update_messages'),
    path('<int:id>', views.edit, name='edit'),
    path('favorite', views.favorite, name='favorite'),
    path('project_detail/<int:project_id>/', views.project_detail, name='project_detail'),
    path('feasibility_study', views.feasibility_study, name='feasibility_study'),
    path('confirmation/', views.confirmation_page, name='confirmation_page'),
    path('services', views.services, name='services'),
    path('chat/<int:feasibility_study_id>/', chat_list, name='chat_list'),
    path('chat/<int:feasibility_study_id>/send/', send_message, name='send_message'),

]


