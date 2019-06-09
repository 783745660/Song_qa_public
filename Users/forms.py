#coding=utf-8
__author__ = 'CoderSong'
__date__ = '2019/5/8 20:10'

from django import forms
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,min_length=7)

class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,min_length=7)

