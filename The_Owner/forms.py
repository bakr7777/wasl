# forms.py

from django import forms
from The_Owner.models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'category', 'description', 'cost', 'details', 'address', 'images']
