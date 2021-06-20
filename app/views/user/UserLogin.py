
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
from app.models import NormalUser


def UserLoginView(request):
    msg = None
    if request.method == 'POST':
        username = request.POST.get("account_no")
        password = request.POST.get("password")
        # user = authenticate(username=username, password=password)
        user = NormalUser.objects.filter(account_no=username).first()
        if user is not None and user.user.is_normaluser:
            if user.user.check_password(password):
                login(request, user)
                return redirect("/dashboard")
            else:
                msg = "incorrect password"
        else:
            msg = 'Invalid credentials'

    return render(request, "user_login.html", {"msg": msg})


