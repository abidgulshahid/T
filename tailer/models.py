from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, BaseUserManager
from tailer.manager import UserManager


# Create your models here.


class Users(AbstractUser):
    email = models.CharField(max_length=100, unique=True)
    is_tailer = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


class Customer(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=500, null=True, blank=True)
    height = models.CharField(max_length=500, null=True, blank=True)
    phone_number = models.CharField(max_length=500, null=True, blank=True)
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
    payment = models.CharField(max_length=500, null=True, blank=True)
    status = [
        ("YES", "YES"),
        ("NO", "NO")
    ]
    recieved = models.CharField(max_length=255, null=True, blank=True, choices=status)
    request_access = models.BooleanField(default=False)


    def __str__(self):
        return str(self.name)


class RequestAccess(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True)
    record_number = models.IntegerField(max_length=255)
