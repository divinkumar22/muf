# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from app.models import PickupMan
from app.views import view,home
from app.views.user import UserHome
from app.views.user import UserLogin,otp_verfiy
from django.urls import path,re_path
from django.contrib.auth.views import LogoutView
from app.views.user import deshborad,transactions
from app.views.pickupman import pickupmanHome,pickupLogin

urlpatterns = [
    path('', home.Home, name='home'),

    # User Side
    path('userHome', UserHome.userHome, name='UserHome'),
    path('userLogin', UserLogin.UserLoginView, name='userLogin'),
    path("logout", LogoutView.as_view(), name="logout"),
    path('otp_verify/<int:pk>', otp_verfiy.Otp_verfiy, name='otp_verfiy'),
    path('dashboard', deshborad.DeshboradVeiw, name='deshborad'),
    path('transactions', transactions.TranactionVeiw, name='transactions'),
    path('PickupMan', pickupmanHome.pickupmanHome, name='pickupman'),
    path('pickupmanlogin', pickupLogin.pickupLoginView, name='pickupmanlogin'),


    # Admin side
    path('MF-admin', view.index, name='MF-admin'),
    re_path(r'^.*\.*', view.pages, name='pages'),
    

   






    # Pickup Man
  


    # Matches any html file
    re_path(r'^.*\.*', view.pages, name='pages'),

]
