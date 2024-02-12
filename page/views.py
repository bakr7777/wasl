from django.shortcuts import redirect, render
from django.shortcuts import render
from The_Owner.models import *
from .models import *
from The_Owner.models import ProjectCategory
from FM.models import PromoRequest
from The_Owner.models import Project
from .models import *
from The_Owner.models import ProjectCategory
from The_Owner.forms import ProjectForm
from FM.models import PromoRequest
from The_Owner.forms import Message
from The_Owner.forms import MessageForm
from The_Investor.models import *

def index(request):
    projects = Project.objects.all()
    categories = ProjectCategory.objects.all()
    promo_requests = PromoRequest.objects.all()  # قم بتحميل طلبات الترويج
    return render(request, 'pages/index.html', {'projects': projects, 'categories': categories, 'promo_requests': promo_requests})


# def index(request):
#     # استرجاع كائنات Project وإرسالها إلى القالب
#     projects = Project.objects.all()
#     return render(request, 'pages/index.html', {'projects': projects} ,)


def about(request):
    return render(request, 'pages/about.html')

def deals(request):
    return render(request, 'pages/deals.html')

def reservation(request):
    if request.method == 'POST':
        add_project =ProjectForm(request.POST, request.FILES)
        if  add_project .is_valid():
            add_project.save()


    context ={
        'projects': Project.objects.all(),
        'form': ProjectForm(),

    }
    return render(request, 'pages/reservation.html' ,context)


def login(request):
    return render(request, 'pages/login.html')

def edit(request, id):
    categories = ProjectCategory.objects.all()
    project_id = Project.objects.get(id=id)
    if request.method == 'POST':
        project_save = ProjectForm(request.POST, request.FILES, instance=project_id)
        if  project_save.is_valid():
            project_save.save()
            return redirect('/')
    else:
        project_save = ProjectForm(instance=project_id)
    context ={'form': project_save,}
    return render(request, 'pages/edit.html' ,context)    

def signIn(request):
    return render(request, 'pages/signIn.html')

def vir(request):
    return render(request, 'pages/vir.html')

def addpost(request):
    return render(request, 'pages/addpost.html')

def promoreq(request):
    return render(request, 'pages/promoreq.html')

def update(request):
    return render(request, 'pages/update.html')

def condations(request):
    return render(request, 'pages/condations.html')

def invreq(request):
    return render(request, 'pages/invreq.html')
def ownpro(request):
    return render(request, 'pages/ownpro.html')
def prodesc(request):
    project = Project.objects.all()
    investment_request = InvestmentRequest.objects.all()
    return render(request, 'pages/prodesc.html', {'project': project,'investment_request': investment_request})


def project(request):
    project = Project.objects.all()
    categories = ProjectCategory.objects.all()
    return render(request, 'pages/project.html', {'project': project, 'categories': categories})

def twsl(request):

    context1 ={
        'Messages': Message.objects.all(),
        'form': MessageForm(),
    }

    if request.method == 'POST':
        add_Message =MessageForm(request.POST, request.FILES)
        if  add_Message .is_valid():
            add_Message.save()

        
    return render(request, 'pages/twsl.html', context1)
    

