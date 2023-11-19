from django.contrib import admin
from .models import Customer, Users, RequestAccess
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register(Customer)
admin.site.register(Users)
admin.site.register(RequestAccess)


