from django import forms
# from  multiupload.fields import MultiFileField
from .models import Project
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project 
        fields = ['owner', 'category', 'title', 'discripe', 'cost', 'details', 'address', 'image', 'active', 'created']

    # images = MultiFileField(min_num=1, max_num=3, max_file_size=1024*1024*5)

########################

from .models import Message

class MessageForm(forms.ModelForm):
    class Meta :
        model = Message
        fields = '__all__'
