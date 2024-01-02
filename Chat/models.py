from django.db import models
from datetime import datetime
from django.conf import settings
from The_Owner.models import *
from The_Investor.models import *


class ChatOwn(models.Model):
    admin = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT,null=True , blank=True )
    owner = models.ForeignKey(Owner, on_delete=models.PROTECT,null=True , blank=True )
    text1 = models.TextField(max_length=200,null=True , blank=True )
    date1 = models.DateField()
    text2 = models.TextField(max_length=200,null=True , blank=True )
    date2 = models.DateField()




class ChatInv(models.Model):
    admin = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT,null=True , blank=True )
    investor = models.ForeignKey(Investor, on_delete=models.PROTECT,null=True , blank=True )
    text1 = models.TextField(max_length=200,null=True , blank=True )
    date1 = models.DateField()
    text2 = models.TextField(max_length=200,null=True , blank=True )
    date2 = models.DateField()
