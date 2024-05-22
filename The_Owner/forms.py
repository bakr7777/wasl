from django import forms
from .models import Project



class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project 
        fields = ['category', 'title', 'discripe', 'cost', 'details', 'address', 'image']
        labels = {
            'category': 'تصنيف المشروع',
            'title': 'اسم المشروع',
            'discripe': 'وصف المشروع',
            'cost': 'تكلفة المشروع',
            'details': 'تفاصيل المشروع',
            'address': 'موقع المشروع',
            'image': 'صورة المشروع',


        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # استخراج المستخدم من الوسائط إذا تم تمريره
        super(ProjectForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['owner'].initial = user.owner.id  # تحديد قيمة حقل المالك بمعرف المالك للمستخدم الحالي
            self.fields['owner'].widget.attrs['readonly'] = True  # جعل حقل المالك لا يقبل التعديل

########################

# from django import forms
# from .models import Project

# class ProjectForm(forms.ModelForm):
#     class Meta:
#         model = Project 
#         fields = ['category', 'title', 'discripe', 'cost', 'details', 'address', 'image', 'active', 'created']
#         labels = {
#             'discripe': 'الوصف المشروع',
#         }


from django import forms
from .models import Message

# class MessageForm(forms.ModelForm):
#     class Meta:
#         model = Message
#         exclude = ['admin_response']  # استثناء admin_response
      # استثناء admin_response
from django import forms
from .models import Message 

class MessageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user and user.is_authenticated:
            self.fields['name'].widget = forms.HiddenInput()
            self.fields['name'].required = False

    class Meta:
        model = Message
        exclude = ['admin_response']

    def clean(self):
        cleaned_data = super().clean()
        user = self.initial.get('user')
        if user and user.is_authenticated:
            cleaned_data['name'] = user.username
        return cleaned_data

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:  # إذا كانت القيمة فارغة
            raise forms.ValidationError("يجب تعبئة هذا الحقل")  # رسالة الخطأ
        return name


# from django import forms
# from .models import ProjectRating

# class ProjectRatingForm(forms.ModelForm):
#     class Meta:
#         model = ProjectRating
#         fields = ['rating', 'comment']  # قم بتضمين حقول التقييم والتعليق من نموذج ProjectRating
#         labels = {
#             'rating': 'التقييم',
#             'comment': 'التعليق',
#         }

# class MessageForm(forms.ModelForm):
#     class Meta:
#         model = Message
#         exclude = ['admin_response']  # استثناء admin_response
        
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         if self.instance and self.instance.name:
#             self.fields['name'].widget = forms.HiddenInput()  # إخفاء حقل الاسم إذا كان المستخدم مسجل دخول

# from django import forms
# from .models import Message

# class MessageForm(forms.ModelForm):
#     class Meta:
#         model = Message
#         exclude = ['admin_response']  # استثناء admin_response
        
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         if self.instance and self.instance.name:
#             self.fields['name'].widget = forms.HiddenInput()  # إخفاء حقل الاسم إذا كان المستخدم مسجل دخول

