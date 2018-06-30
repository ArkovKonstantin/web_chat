# -*- coding: utf-8 -*-
from django import forms
from .models import *


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(min_length=5)
    password = forms.CharField(min_length=8)
    password2 = forms.CharField(min_length=8)
    email = forms.EmailField(label='Почта')

    class Meta:
        model = ChatUser
        exclude = ["user", "friends"]
        widgets = {

        }


class LoginForm(forms.Form):
    username = forms.CharField(min_length=5, label='Логин')
    password = forms.CharField(min_length=8, label='Пароль')


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text', ]


class SearchForm(forms.Form):
    query = forms.CharField()
