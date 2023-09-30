from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Tailor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=500, null=True, blank=True)
    height = models.CharField(max_length=500, null=True, blank=True)
    phone_number = models.CharField(max_length=500, null=True, blank=True)
    chest = models.CharField(max_length=500, null=True, blank=True)
    right_shoulder = models.CharField(max_length=500, null=True, blank=True)
    left_shoulder = models.CharField(max_length=500, null=True, blank=True)
    type = models.CharField(max_length=500, null=True, blank=True)
    upper_shirt = models.CharField(max_length=500, null=True, blank=True)
    trouser = models.CharField(max_length=500, null=True, blank=True)
    order_take =  models.DateField(null=True, blank=True)
    order_deadline =  models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.name)


