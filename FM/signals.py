from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PromoRequest, InvestmentRequest, FinancialReport
from django.utils import timezone
from datetime import datetime

@receiver(post_save, sender=PromoRequest)
def check_promo_request_expiration(sender, instance, **kwargs):
    instance.check_expiration()

@receiver(post_save, sender=InvestmentRequest)
def update_investment_report(sender, instance, **kwargs):
    today = timezone.now().date()
    # FinancialReport.objects.filter(date=today).exclude(id=FinancialReport.objects.filter(date=today).first().id).delete()
    report, created = FinancialReport.objects.get_or_create(date=today)
    report.generate_report()

@receiver(post_save, sender=PromoRequest)
def update_promo_report(sender, instance, **kwargs):
    today = timezone.now().date()
    # FinancialReport.objects.filter(date=today).exclude(id=FinancialReport.objects.filter(date=today).first().id).delete()
    report, created = FinancialReport.objects.get_or_create(date=today)
    report.generate_report()
