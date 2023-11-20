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
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='user')
    tailer = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='tailer')
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

    COLOR_CHOICES = [
        ('red', 'Red'),
        ('green', 'Green'),
        ('blue', 'Blue'),
        ('yellow', 'Yellow'),
        ('magenta', 'Magenta'),
        ('cyan', 'Cyan'),
        ('orange', 'Orange'),
        ('purple', 'Purple'),
        ('darkgreen', 'Dark Green'),
        ('navy', 'Navy'),
        ('pink', 'Pink'),
        ('saddlebrown', 'Saddle Brown'),
        ('brown', 'Brown'),
        ('gray', 'Gray'),
        ('black', 'Black'),
    ]
    cloth_color = models.CharField(max_length=500, null=True, blank=True, choices=COLOR_CHOICES)
    cloth_price = models.CharField(max_length=500, null=True, blank=True)
    recieved_status = [
        ("YES", "YES"),
        ("NO", "NO")
    ]
    recieved = models.CharField(max_length=255, null=True, blank=True, choices=recieved_status)
    cloth_type_status = [
        ("Cotton", "Cotton"),
        ("Fabric", "Fabric"),
        ("Silk", "Silk"),
        ("Linen", "Linen"),
    ]
    cloth_quantites = models.CharField(max_length=255, null=True, blank=True)
    cloth_types = models.CharField(max_length=255, null=True, blank=True, choices=cloth_type_status)
    request_access = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    status = [
        ("Waiting", "Waiting"),
        ("Ready", "Ready")
    ]
    status = models.CharField(max_length=255, null=True, blank=True, choices=status, default='Waiting')
    pant_length =  models.CharField(max_length=255, null=True, blank=True)
    pant_width =  models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return str(self.name)


class RequestAccess(models.Model):
    requested_by = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='request_by_usr', null=True,
                                     blank=True)
    record_number = models.IntegerField(max_length=255)
    requested_to = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='request_to_user', null=True,
                                     blank=True)
    is_approved = models.BooleanField(default=False)
