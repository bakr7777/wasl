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
from django.shortcuts import render
from .models import *
from django.shortcuts import render, redirect
from django.contrib import messages




def index(request):
    projects = Project.objects.all()
    categories = ProjectCategory.objects.all()
    promo_requests = PromoRequest.objects.all()  # قم بتحميل طلبات الترويج
    total_projects = Project.objects.count()
    total_investor = Investor.objects.count()
    total_owners = Owner.objects.count()

    return render(request, 'pages/index.html', {'projects': projects, 'categories': categories, 'promo_requests': promo_requests, 'total_projects': total_projects ,'total_investor': total_investor, 'total_owners': total_owners})



def about(request):
    return render(request, 'pages/about.html')

def deals(request):
    projects = Project.objects.all()
    categories = ProjectCategory.objects.all()
    promo_requests = PromoRequest.objects.all()  # قم بتحميل طلبات الترويج
    return  render(request, 'pages/deals.html' , {'projects': projects, 'categories': categories, 'promo_requests': promo_requests})

# def reservation(request):
#     if request.method == 'POST':
#         add_project =ProjectForm(request.POST, request.FILES)
#         if  add_project .is_valid():
#             add_project.save()


#     context ={
#         'projects': Project.objects.all(),
#         'form': ProjectForm(),

#     }
#     return render(request, 'pages/reservation.html' ,context)
# views.py


# def reservation(request):
#     if request.method == 'POST':
#         add_project = ProjectForm(request.POST, request.FILES)
#         if add_project.is_valid():
#             project_instance = add_project.save()

#     context = {
#         'projects': Project.objects.all(),
#         'form': ProjectForm(),
#     }
#     return render(request, 'pages/reservation.html', context)

from django.shortcuts import render
from The_Owner.forms import ProjectForm

def reservation(request):
    if request.method == 'POST':
        # إنشاء نموذج المشروع مع البيانات المدخلة
        add_project = ProjectForm(request.POST, request.FILES)
        if add_project.is_valid():
            # حفظ المشروع مع تعيين owner تلقائيًا
            project_instance = add_project.save(commit=False)
            project_instance.owner = request.user.owner  # تحديد الـ owner تلقائيًا
            project_instance.save()

    # جلب جميع المشاريع من قاعدة البيانات
    projects = Project.objects.all()
    # إعادة إنشاء نموذج المشروع لعرضه في الصفحة
    form = ProjectForm()

    context = {
        'projects': projects,
        'form': form,
    }
    return render(request, 'pages/reservation.html', context)



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


# def project(request):
#     project = Project.objects.all()
#     categories = ProjectCategory.objects.all()
#     return render(request, 'pages/project.html', {'project': project, 'categories': categories})
from django.shortcuts import redirect
from django.urls import reverse

def project(request):
    if request.user.is_authenticated:
        # التأكد من أن المستخدم مسجل الدخول
        owner = request.user.owner  # الحصول على مالك المشروع الحالي

        # عرض مشاريع المالك الحالي فقط
        projects = Project.objects.filter(owner=owner)
        
        return render(request, 'pages/project.html', {'projects': projects})
    else:
        # إعادة توجيه المستخدم إلى صفحة تسجيل الدخول
        return redirect(reverse('login'))
# في ملف views.pyfrom django.shortcuts import render, redirect
from The_Owner.models import Message
from The_Owner.forms import MessageForm

def twsl(request):
    user_messages = None  # يمكنك إعداده لقائمة فارغة أو None، اعتمادًا على ما تفضله

    if request.method == 'POST':
        add_Message = MessageForm(request.POST, request.FILES)
        if add_Message.is_valid():
            message_instance = add_Message.save(commit=False)
            if request.user.is_authenticated:
                message_instance.name = request.user
            message_instance.save()
            return redirect('twsl')  # بعد إرسال الرسالة بنجاح، قم بتوجيه المستخدم مباشرة إلى صفحة twsl

    if request.user.is_authenticated:
        user_messages = Message.objects.filter(name=request.user)

    context = {
        'Messages': user_messages,
        'form': MessageForm(user=request.user if request.user.is_authenticated else None),
    }

    return render(request, 'pages/twsl.html', context)



    
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from The_Investor.models import Project, InvestmentRequest
from The_Owner.models import Project
from The_Owner.forms import ProjectRatingForm






@login_required
def prodesc(request):
    investor = request.user.investor
    
    if request.method == 'POST':
        project_id = request.POST.get('project')
        project = Project.objects.get(id=project_id)

        favorite, created = Favorite.objects.get_or_create(investor=investor, project=project)

        return redirect('favorite')

    investment_requests = InvestmentRequest.objects.filter(investor=investor)
    
    # إضافة النموذج لإضافة التعليقات والتقييمات
    if request.method == 'POST':
        form = ProjectRatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.user = request.user
            rating.project = project
            rating.save()
            return redirect('prodesc')  # اسم العرض الحالي
    else:
        form = ProjectRatingForm()
        
    return render(request, 'pages/prodesc.html', {'investment_requests': investment_requests, 'form': form})


# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render, redirect
# from The_Investor.models import Project, InvestmentRequest
# from The_Owner.models import Project
# from The_Owner.forms import ProjectRatingForm



# @login_required
# def prodesc(request):
#     investor = request.user.investor
    
#     if request.method == 'POST':
#         project_id = request.POST.get('project')
#         project = Project.objects.get(id=project_id)
        
#         # إضافة التعليقات والتقييمات
#         form = ProjectRatingForm(request.POST)
#         if form.is_valid():
#             rating = form.save(commit=False)
#             rating.user = request.user
#             rating.project = project
#             rating.save()
#             return redirect('prodesc')  # اسم العرض الحالي
#     else:
#         form = ProjectRatingForm()

#     investment_requests = InvestmentRequest.objects.filter(investor=investor)
    
#     return render(request, 'pages/prodesc.html', {'investment_requests': investment_requests, 'form': form})




from django.contrib.auth.models import User

def favorite(request):
    # التأكد من تسجيل الدخول
    if request.user.is_authenticated:
        # استعلام للحصول على المستثمر الحالي
        current_investor = Investor.objects.get(user=request.user)
        # استعلام للحصول على المفضلات الخاصة بالمستثمر الحالي فقط
        favorite = Favorite.objects.filter(investor=current_investor)
        # إرجاع الاستجابة مع قائمة المفضلات
        return render(request, 'pages/favorite.html', {'favorite': favorite})
    else:
        # إذا لم يكن المستخدم مسجل الدخول، يتم توجيهه إلى صفحة تسجيل الدخول أو أي صفحة أخرى حسب التصميم الخاص بك
        return redirect('login')
