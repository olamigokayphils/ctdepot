from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from .models import MyUser

admin.site.register(MyUser)

from .models import Meat, Wallet, Order

admin.site.register(Meat)
admin.site.register(Wallet)
admin.site.register(Order)