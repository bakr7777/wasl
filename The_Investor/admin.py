from django.contrib import admin
from .models import Investor , Favorite , InvestmentRequest, InvestorRatingComment



admin.site.register(Investor)
admin.site.register(Favorite)
admin.site.register(InvestmentRequest)
admin.site.register(InvestorRatingComment)

