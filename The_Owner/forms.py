# forms.py

from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

########################

from .models import Message

class MessageForm(forms.ModelForm):
    class Meta :
        model = Message
        fields = '__all__'
