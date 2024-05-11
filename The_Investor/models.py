from django.db import models
from datetime import datetime
from django.conf import settings
from The_Owner.models import *
from django.contrib.auth.models import User 


###################################investor#######################
class Investor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='usersphoto/%Y/%m/%d/',blank=True)
    phone = models.CharField(max_length=9)
    address = models.CharField(max_length=25)
    total_investor = models.IntegerField(default=0)
    
    
    def __str__(self):
        return f"Total investor: {self.total_investor}"
    def __str__(self):
        return f'Profile of {self.user.username}'


###################################investor#######################

class Favorite(models.Model):
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE,null=True , blank=True )
    project = models.ForeignKey(Project, on_delete=models.CASCADE,null=True , blank=True)
    def __str__(self):
        return f"investor: {self.investor}"

  

########################################invrequest#######################

class InvestmentRequest(models.Model):
    date = models.DateTimeField(default=datetime.now)
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE,null=True , blank=True )
    project = models.ForeignKey(Project, on_delete=models.CASCADE,null=True , blank=True )
    is_allowed = models.BooleanField(default=True)  # حقل جديد لتحديد ما إذا كان الطلب مسموحًا بعرضه أم لا

    def __str__(self):
        return f'InvestmentRequest: {self.investor}'

    


