# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from app.models import NormalUser, PickupMan, User,Transaction, Otp


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'pickup_man', 'created_at', 'updated_at')


admin.site.register(User)
admin.site.register(PickupMan)
admin.site.register(NormalUser)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Otp)