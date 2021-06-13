# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from app.models import User,PickupMan,SuperUser,Transaction,Otp

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user','pickup_man','created_at','updated_at')



# Register your models here.
admin.site.register(User)
admin.site.register(PickupMan)
admin.site.register(SuperUser)
admin.site.register(Transaction,TransactionAdmin)
admin.site.register(Otp)