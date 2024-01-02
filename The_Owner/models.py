from django.db import models
from datetime import datetime
from django.conf import settings

##############################OWner##################################################

class Owner(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='usersphoto/%Y/%m/%d/',blank=True)
    address = models.CharField(max_length=25,null=True)
    phone = models.CharField(max_length=9)
    def __str__(self):
        return f'Profile of {self.user.username}'


##############################Category##################################################

class ProjectCategory(models.Model):
    category = models.TextField(max_length=50)
    def __str__(self):
        return self.category


##############################Project##################################################

class Project(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE,null=True , blank=True )
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE,null=True , blank=True )
    title = models.CharField(max_length=100)
    discripe = models.TextField(max_length=200)
    cost = models.DecimalField(max_digits=5, decimal_places=2)
    details = models.TextField(max_length=1000)
    address = models.CharField(max_length=30)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.title

##############################Photo##################################################

class Photo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE,null=True , blank=True )
    photo_path = models.TextField(max_length=200)
