# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from app.models import PickupMan, User, Otp


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",                
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",                
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password check",                
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class OTPForm(forms.ModelForm):
    class Meta:
        model = Otp
        fields = ['otp']


class pickupmanLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']