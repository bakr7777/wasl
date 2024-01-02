from django.db import models
from datetime import datetime
from django.conf import settings
from The_Owner.models import *
from The_Investor.models import *



################################promotype######################


class Promotype(models.Model):
    promo_name = models.CharField(max_length=25)
    promo_cost = models.DecimalField(max_digits=5, decimal_places=2)
    during = models.CharField(max_length=25)
    def __str__(self):
        return self.promo_name

##########################promorequest########################


class PromoRequest(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE,null=True , blank=True )
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE,null=True , blank=True )
    promo_type = models.ForeignKey(Promotype, on_delete=models.CASCADE,null=True , blank=True )
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


##########################FM########################


class FinancialMovement(models.Model):
    investmentRequest = models.ForeignKey(InvestmentRequest , on_delete=models.CASCADE,null=True , blank=True )
    promoRequest = models.ForeignKey(PromoRequest , on_delete=models.CASCADE,null=True , blank=True )
    statement = models.CharField(max_length= 50)
    income = models.DecimalField(max_digits=5, decimal_places=2)
    outcome = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateTimeField(default=datetime.now)
    pay_method = models.CharField(max_length=50 , null=True)
