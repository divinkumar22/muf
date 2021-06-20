from django import forms
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse



def pickupLoginView(request):
    # form = pickupmanLoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)
        user = authenticate(username=username, password=password)
        print(user)

        if user is not None:
            if user.is_pickupman:
                login(request, user)
                return redirect("/dashboard")
            else:
                msg = "username or password is incorrect."
        else:
            msg = 'Invalid credentials'
    
    return render(request, "pickmanlogin.html", {"msg": msg})


