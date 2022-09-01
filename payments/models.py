from django.db import models

# Create your models here.
PAYMENT_STATUSES = (
    ("succeeded", "Success"),
    ("failed", "Failed"),
)

class Payment(models.Model):
    payment_ref = models.CharField(max_length=200, unique=True)
    email = models.EmailField()
    name = models.CharField(max_length=200, null=True, blank=True)
    currency = models.CharField(max_length=20)
    amount = models.FloatField(default=0)
    date_paid = models.DateField()
    status = models.CharField(max_length=200, choices=PAYMENT_STATUSES)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.payment_ref
