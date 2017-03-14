#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Artist
from django import forms
from django.utils.translation import ugettext_lazy as _




class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ('name', 'email')
        labels = {
            'name': _('ФИО'),
            'email': _('E-mail'),
        }
        widgets = {
            'name': forms.TextInput({'placeholder': 'ФИО'}),
            'email': forms.EmailInput({'placeholder': 'E-mail'}),
        }



class UserAuth(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    class Meta:
        model = Artist
        fields = ('email', 'password')
        widgets = {
            'email': forms.TextInput({'placeholder': 'Логин (почта, указанная при регистрации)', 'id': '21285'}),

        }

class registrationFull(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    passwordCheck = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Подтверждение пароля'}))
    class Meta:
        model = Artist
        fields = ('name', 'email', 'city', 'age', 'favorite', 'password', 'passwordCheck')
        labels = {
            'name': _('ФИО'),
            'email': _('E-mail'),
        }
        widgets = {
            'name': forms.TextInput({'placeholder': 'ФИО', 'required': 'true'}),
            'email': forms.EmailInput({'placeholder': 'E-mail'}),
            'city': forms.TextInput({'placeholder': 'Город'}),
            'age': forms.NumberInput({'placeholder': 'Возраст'}),
            'favorite': forms.Select({'placeholder': 'Любимый инструмент'}),

        }

class changePersonal(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ('name', 'city', 'age', 'favorite')
        labels = {

        }
        widgets = {
            'name': forms.TextInput({'placeholder': 'ФИО'}),
            'city': forms.TextInput({'placeholder': 'Город'}),
            'age': forms.NumberInput({'placeholder': 'Возраст'}),
            'favorite': forms.Select({'placeholder': 'Любимый инструмент'}),
        }

class passwordChange(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    passwordCheck = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Подтверждение пароля'}))
    class Meta:
        model = Artist
        fields = ('password', 'passwordCheck')
        labels = {

        }
        widgets = {

        }

class forgetPass(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ('email', 'age')
        labels = {

        }
        widgets = {
            'email': forms.TextInput({'placeholder': 'Почта'}),
            'age': forms.NumberInput({'placeholder': 'Возраст'}),
        }
