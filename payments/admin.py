from django.contrib import admin
from .models import Payment
# Register your models here.
class PaymentAdmin(admin.ModelAdmin):
    list_display = ["payment_ref", "name", "email", "amount", "currency", "status", "date_paid", "date_created", "date_updated"]

admin.site.register(Payment, PaymentAdmin)