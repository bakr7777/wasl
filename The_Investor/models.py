from django.db import models
from datetime import datetime
from django.conf import settings
from The_Owner.models import *


###################################investor#######################
class Investor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='usersphoto/%Y/%m/%d/',blank=True)
    phone = models.CharField(max_length=9)
    address = models.CharField(max_length=25)
    def __str__(self):
        return f'Profile of {self.user.username}'


###################################investor#######################

class Favorite(models.Model):
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE,null=True , blank=True )
    project = models.ForeignKey(Project, on_delete=models.CASCADE,null=True , blank=True)

########################################invrequest#######################

class InvestmentRequest(models.Model):
    date = models.DateTimeField(default=datetime.now)
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE,null=True , blank=True )
    project = models.ForeignKey(Project, on_delete=models.CASCADE,null=True , blank=True )