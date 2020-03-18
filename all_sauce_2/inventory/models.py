from django.db import models
from datetime import datetime, timedelta

# Create your models here.

class Sauce(models.Model):

    def get_expiry_date():
        return datetime.today() + timedelta(days=90)

    name = models.CharField(max_length=50)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    location = models.CharField(max_length=50)
    purchase_date = models.DateField(default=datetime.now)
    expriy_date = models.DateField(default=get_expiry_date)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Sauce_detail", kwargs={"pk": self.pk})
