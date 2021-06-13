from django import forms
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse
from authentication.forms import UserLoginForm,pickupmanLoginForm
from app.models import User,Otp,PickupMan
from authentication.otp import OTP
from datetime import datetime

def pickupLoginView(request):
    form = pickupmanLoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            print(username,password)
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return HttpResponse("done")
            else:
                
                msg = 'Invalid credentials'
        else:
            
            msg = 'Error validating the form'
    
    return render(request, "pickmanlogin.html", {"form": form, "msg" : msg})


