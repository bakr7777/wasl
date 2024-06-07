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
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.contrib import messages


from django.shortcuts import render, get_object_or_404
from django.db.models import Avg
from The_Owner.models import Project, ProjectCategory
from The_Investor.models import Investor, Owner
from FM.models import PromoRequest

def index(request):
    projects = Project.objects.all()
    categories = ProjectCategory.objects.all()
    promo_requests = PromoRequest.objects.filter(active=True)

    # تحقق من انتهاء صلاحية جميع طلبات الترويج
    for promo_request in promo_requests:
        promo_request.check_expiration()

    promo_requests = PromoRequest.objects.filter(active=True)  # إعادة التصفية بعد التحقق

    total_projects = Project.objects.count()
    total_investor = Investor.objects.count()
    total_owners = Owner.objects.count()
    total_investmentrequest = InvestmentRequest.objects.filter(is_allowed=True).count()
   
    # حساب متوسط التقييم لكل مشروع
    for project in projects:
        project.average_rating = project.investorratingcomment_set.aggregate(Avg('rating'))['rating__avg']

    for promo_request in promo_requests:
        promo_request.title_length = len(promo_request.project.title)

    return render(request, 'pages/index.html', {
        'projects': projects,
        'categories': categories,
        'promo_requests': promo_requests,
        'total_projects': total_projects,
        'total_investor': total_investor,
        'total_owners': total_owners
    })


def about(request):
    return render(request, 'pages/about.html')

def deals(request):
    projects = Project.objects.all()
    categories = ProjectCategory.objects.all()
   
    return render(request, 'pages/deals.html', {
        'projects': projects,
        'categories': categories,
       
    })
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
from django.db.models import Avg

def project_detail(request, project_id,):
    investor = request.user.investor
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        investor = request.user.investor
        project = get_object_or_404(Project, id=project_id)
    
    if request.method == 'POST':
        investor_id = request.POST.get('investor')
        project_id = request.POST.get('project')

        if investor_id and project_id:
            investor = Investor.objects.get(id=investor_id)
            project = Project.objects.get(id=project_id)
            Favorite.objects.get_or_create(investor=investor, project=project)
            return redirect('favorite')
   

    # حساب متوسط التقييم
    average_rating = project.investorratingcomment_set.aggregate(Avg('rating'))['rating__avg']   
    
    return render(request, 'pages/project_detail.html', {'project': project, 'average_rating': average_rating, 'status': 'failed'}, status=400)

def condations(request):
    return render(request, 'pages/condations.html')


def ownpro(request):
    return render(request, 'pages/ownpro.html')


# def project(request):
#     project = Project.objects.all()
#     categories = ProjectCategory.objects.all()
#     return render(request, 'pages/project.html', {'project': project, 'categories': categories})
from django.shortcuts import redirect
from django.urls import reverse

def project(request):
    print("Entered project view")
    try:  
        if not request.user.is_authenticated:
           messages.error(request, 'يرجى تسجيل الدخول للوصول إلى هذه الصفحة.')
           print("User not authenticated")
           return redirect('login')

        owner = request.user.owner
        print("Owner retrieved:", owner)

        if hasattr(owner, 'investor') and owner.investor:
           messages.error(request, 'ليس لديك صلاحية الوصول إلى هذه الصفحة.')
           print("Owner is an investor")
           return redirect('index')   
         
        if request.user.is_authenticated:
            # التأكد من أن المستخدم مسجل الدخول
            owner = request.user.owner  # الحصول على مالك المشروع الحالي

            # عرض مشاريع المالك الحالي فقط
            projects = Project.objects.filter(owner=owner)
            
            return render(request, 'pages/project.html', {'projects': projects})
        else:
            # إعادة توجيه المستخدم إلى صفحة تسجيل الدخول
            return redirect(reverse('login'))
     
    except AttributeError:
        messages.error(request, ' project لاتوجد لك صلاحية بالدخول الى صفحة')
        print("AttributeError: No access rights")
        return redirect('index')  # أو أي صفحة أخرى تريد إعادة التوجيه إليها
    
        

# في ملف views.pyfrom django.shortcuts import render, redirect
from The_Owner.models import Message
from The_Owner.forms import MessageForm


# def twsl(request):
#     user_messages = None  # يمكنك إعداده لقائمة فارغة أو None، اعتمادًا على ما تفضله

#     if request.method == 'POST':
#         add_Message = MessageForm(request.POST, request.FILES)
#         if add_Message.is_valid():
#             message_instance = add_Message.save(commit=False)
#             if request.user.is_authenticated:
#                 message_instance.name = request.user
#             message_instance.save()
#             return redirect('twsl')  # بعد إرسال الرسالة بنجاح، قم بتوجيه المستخدم مباشرة إلى صفحة twsl

#     if request.user.is_authenticated:
#         user_messages = Message.objects.filter(name=request.user)

#     context = {
#         'Messages': user_messages,
#         'form': MessageForm(user=request.user if request.user.is_authenticated else None),
#     }

#     return render(request, 'pages/twsl.html', context)



@login_required
def twsl(request):
    user_messages = None

    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            message_instance = form.save(commit=False)
            if request.user.is_authenticated:
                message_instance.name = request.user
            message_instance.save()
            return redirect('twsl')  # بعد إرسال الرسالة بنجاح، قم بتوجيه المستخدم مباشرة إلى صفحة twsl

    if request.user.is_authenticated:
        user_messages = Message.objects.filter(name=request.user)
        # تحديد جميع الرسائل غير المقروءة وتحديثها عند عرض صفحة الرسائل
        unread_messages = user_messages.filter(is_read=False)
        unread_messages.update(is_read=True)

    context = {
        'Messages': user_messages,
        'form': MessageForm(user=request.user if request.user.is_authenticated else None),
    }

    return render(request, 'pages/twsl.html', context)

# ######تحديث صفحة المراسلة :-

# @login_required
# def update_messages(request):
#     if request.method == 'GET' and request.user.is_authenticated:
#         # احصل على الرسائل الجديدة من قاعدة البيانات
#         user_messages = Message.objects.filter(name=request.user)
#         unread_messages = user_messages.filter(is_read=False)
#         unread_messages.update(is_read=True)

#         # إرجاع الرد بنجاح
#         return JsonResponse({'success': True})
#     else:
#         # في حالة عدم توفر صلاحيات أو طلب غير صحيح
#         return JsonResponse({'success': False}, status=400)



    
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from The_Investor.forms import RatingCommentForm
from The_Investor.models import InvestmentRequest, InvestorRatingComment

from django.shortcuts import get_object_or_404
from The_Investor.models import InvestorRatingComment

# @login_required
# def prodesc(request):
#     investor = request.user.investor

#     if request.method == 'POST':
#         form = RatingCommentForm(request.POST)
#         if form.is_valid():
#             rating_comment = form.save(commit=False)
#             rating_comment.investor = investor
#             project_id = request.POST.get('project_id')
#             investment_request = InvestmentRequest.objects.get(project_id=project_id, investor=investor)
#             rating_comment.project = investment_request.project
#             rating_comment.save()
#             return redirect('prodesc')
#     else:
#         form = RatingCommentForm()

#     investment_requests = InvestmentRequest.objects.filter(investor=investor)

#     return render(request, 'pages/prodesc.html', {'investment_requests': investment_requests, 'form': form}) هذا رقم واحد والي تحته اثنين

@login_required
def prodesc(request):
    print("Entered prodesc view")
    try:  
        if not request.user.is_authenticated:
           messages.error(request, 'يرجى تسجيل الدخول للوصول إلى هذه الصفحة.')
           print("User not authenticated")
           return redirect('login')

        investor = request.user.investor
        print("Investor retrieved:", investor)

        if hasattr(investor, 'owner') and investor.owner:
           messages.error(request, 'ليس لديك صلاحية الوصول إلى هذه الصفحة.')
           print("Investor is an owner")
           return redirect('index')


        if request.method == 'POST':
            form = RatingCommentForm(request.POST)
            if form.is_valid():
                rating_comment = form.save(commit=False)
                rating_comment.investor = investor
                project_id = request.POST.get('project_id')
                investment_request = InvestmentRequest.objects.get(project_id=project_id, investor=investor)
                rating_comment.project = investment_request.project

                try:
                    rating_comment.save()
                except IntegrityError:
                    # يمكن هنا إضافة رسالة للمستخدم توضح أنه قد قام بتقييم هذا المشروع مسبقاً
                    form.add_error(None, "لقد قمت بتقييم هذا المشروع مسبقاً.")
                    return redirect('prodesc')

                return redirect('prodesc')
        else:
            form = RatingCommentForm()

        investment_requests = InvestmentRequest.objects.filter(investor=investor)
        rated_projects = InvestorRatingComment.objects.filter(investor=investor).values_list('project_id', flat=True)

        context = {
            'investment_requests': investment_requests,
            'form': form,
            'rated_projects': rated_projects
        }
        
        if request.method == 'POST':
            projectid = request.POST.get('project')
            investorid = request.POST.get('investor')

            project = Project.objects.get(id = projectid)
            investor =  Investor.objects.get(id = investorid)


            Favorite.objects.get_or_create(investor=investor , project=project)
            return redirect('favorite')
        
    
        project = Project.objects.all()
        investment_request = InvestmentRequest.objects.all()


        return render(request, 'pages/prodesc.html', context)
    
    except AttributeError:
        messages.error(request, ' prodesc لاتوجد لك صلاحية بالدخول الى صفحة')
        print("AttributeError: No access rights")
        return redirect('index')  # أو أي صفحة أخرى تريد إعادة التوجيه إليها

from django.contrib.auth.models import User

def favorite(request):
    if request.method == 'POST':
        project_id = request.POST.get('project_id')
        
        try:
            current_investor = Investor.objects.get(user=request.user)
        except Investor.DoesNotExist:
            # تعامل مع الحالة حيث لا يوجد مستثمر مرتبط بالمستخدم الحالي
            return render(request, 'error.html', {'message': 'Investor does not exist'})

        favorite = get_object_or_404(Favorite, investor=current_investor, project_id=project_id)
        favorite.delete()
        return redirect('favorite')
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
from django.shortcuts import render, redirect
from Chat.forms import FeasibilityStudyRequestForm 

def feasibility_study(request):
    if request.method == 'POST':
        form = FeasibilityStudyRequestForm(request.POST, request.FILES)
        if form.is_valid():
            request_instance = form.save(commit=False)
            request_instance.user = request.user
            request_instance.save()
            return redirect('confirmation_page')  # تأكد من وجود صفحة تأكيد
    else:
        form = FeasibilityStudyRequestForm()
    return render(request, 'pages/feasibility_study.html', {'form': form})



def confirmation_page(request):
    return render(request, 'pages/confirmation_page.html')

from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render
from Chat.models import FeasibilityStudyRequest
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Chat.models import FeasibilityStudyRequest, FeasibilityStudy, Chat
from Chat.forms import ChatForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Chat.models import FeasibilityStudyRequest, FeasibilityStudy, Chat
from Chat.forms import ChatForm

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from Chat.models import FeasibilityStudyRequest, FeasibilityStudy, Chat
from Chat.forms import ChatForm

@login_required
def services(request):
    user_requests = FeasibilityStudyRequest.objects.filter(user=request.user)
    user_feasibility_studies = []

    for feasibility_request in user_requests:
        if feasibility_request.is_allowed:
            studies = feasibility_request.feasibility_studies.all()
            user_feasibility_studies.extend(studies)

    return render(request, 'pages/services.html', {
        'user_feasibility_studies': user_feasibility_studies,
        'user_requests': user_requests
    })
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from Chat.models import FeasibilityStudy, Chat
from Chat.forms import ChatForm

@login_required
def chat_list(request, feasibility_study_id):
    feasibility_study = get_object_or_404(FeasibilityStudy, id=feasibility_study_id)
    chats = Chat.objects.filter(feasibility_study=feasibility_study).order_by('date')

    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            chat = form.save(commit=False)
            if request.user.is_staff:
                chat.admin = request.user
            elif hasattr(request.user, 'owner'):
                chat.owner = request.user.owner
            elif hasattr(request.user, 'investor'):
                chat.investor = request.user.investor
            chat.feasibility_study = feasibility_study
            chat.save()
            return redirect('chat_list', feasibility_study_id=feasibility_study_id)
    else:
        form = ChatForm()

    return render(request, 'pages/chat_list.html', {
        'feasibility_study': feasibility_study,
        'chats': chats,
        'form': form,
    })

@login_required
def send_message(request, feasibility_study_id):
    feasibility_study = get_object_or_404(FeasibilityStudy, id=feasibility_study_id)
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            chat = form.save(commit=False)
            chat.admin = request.user
            chat.feasibility_study = feasibility_study
            chat.save()
            return redirect('chat_list', feasibility_study_id=feasibility_study_id)
    else:
        form = ChatForm()
    return render(request, 'pages/send_message.html', {'form': form, 'feasibility_study': feasibility_study})
