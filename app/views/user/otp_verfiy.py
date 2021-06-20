from authentication.otp import OTP
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import forms, template
from app.models import Otp,User
from authentication.forms import OTPForm



def Otp_verfiy(request,pk):
    print(request.POST.__dict__)
    if request.method == 'POST':
        print("user")
        user = User.objects.filter(pk = pk).first()
        print(user)
        form = OTPForm(request.POST or None)
        if form.is_valid():
            otp = form.cleaned_data.get("otp")
            if user:
                userotp = Otp.objects.filter(user=user).first()
                user_otp = userotp.otp
                if otp == user_otp:
                    print("done")
                    return render(request,"otp.html")
                else:
                    return HttpResponse("enter valid otp")

            else:
                print("hllwwwwwww")
                return render(request, "otp.html")
        else:
            print(form.errors.as_data)
            return render(request, "otp.html")
                
    else:
        
        return render(request,"otp.html")

            

    




    
   