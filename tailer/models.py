from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=500, null=True, blank=True)
    height = models.CharField(max_length=500, null=True, blank=True)
    phone_number = models.IntegerField(max_length=500, null=True, blank=True)
    chest = models.CharField(max_length=500, null=True, blank=True)
    right_shoulder = models.CharField(max_length=500, null=True, blank=True)
    left_shoulder = models.CharField(max_length=500, null=True, blank=True)
    type = models.CharField(max_length=500, null=True, blank=True)
    upper_shirt = models.CharField(max_length=500, null=True, blank=True)
    trouser = models.CharField(max_length=500, null=True, blank=True)
    order_take = models.DateField(null=True, blank=True)
    order_deadline = models.DateField(null=True, blank=True)
    father_name = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    length = models.CharField(max_length=255, null=True, blank=True)
    cuff = models.CharField(max_length=255, null=True, blank=True)
    waist = models.CharField(max_length=255, null=True, blank=True)
    low_waist = models.CharField(max_length=255, null=True, blank=True)
    hip = models.CharField(max_length=255, null=True, blank=True)
    muscle = models.CharField(max_length=255, null=True, blank=True)
    arm_hole = models.CharField(max_length=255, null=True, blank=True)
    collar = models.CharField(max_length=255, null=True, blank=True)
    pocket = models.CharField(max_length=255, null=True, blank=True)
    pancha = models.CharField(max_length=255, null=True, blank=True)
    extra_info = models.CharField(max_length=500, null=True, blank=True)
    payment = models.IntegerField(null=True)
    status = [
        ("YES", "YES"),
        ("NO", "NO")
    ]
    recieved = models.CharField(max_length=255, null=True, blank=True, choices=status)


    def __str__(self):
        return str(self.name)
