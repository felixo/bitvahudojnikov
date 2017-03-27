#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Artist, Task_1, Task_2, Task_3, Task_4, Task_5, Task_6, Task_7, Jury
from django.contrib.auth.models import User
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
            'email': forms.EmailInput({'placeholder': 'E-mail','required': 'true'}),
            'city': forms.TextInput({'placeholder': 'Город', 'required': 'true'}),
            'age': forms.NumberInput({'placeholder': 'Возраст', 'required': 'true'}),
            'favorite': forms.Select({'placeholder': 'Любимый инструмент', 'required': 'true'}),

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

class loadArt1(forms.ModelForm):
    class Meta:
        model = Task_1
        fields = ('docfile','visible')
        widgets = {
            'docfile': forms.FileInput({'id': 'fileway1'}),
        }

class loadArt2(forms.ModelForm):
    class Meta:
        model = Task_2
        fields = ('docfile','visible')
        widgets = {
            'docfile': forms.FileInput({'id': 'fileway2'}),
        }

class loadArt3(forms.ModelForm):
    class Meta:
        model = Task_3
        fields = ('docfile','visible')
        widgets = {
            'docfile': forms.FileInput({'id': 'fileway3'}),
        }

class loadArt4(forms.ModelForm):
    class Meta:
        model = Task_4
        fields = ('docfile','visible')
        widgets = {
            'docfile': forms.FileInput({'id': 'fileway4'}),
        }

class loadArt5(forms.ModelForm):
    class Meta:
        model = Task_5
        fields = ('docfile','visible')
        widgets = {
            'docfile': forms.FileInput({'id': 'fileway5'}),
        }

class loadArt6(forms.ModelForm):
    class Meta:
        model = Task_6
        fields = ('docfile','visible')
        widgets = {
            'docfile': forms.FileInput({'id': 'fileway6'}),
        }

class loadArt7(forms.ModelForm):
    class Meta:
        model = Task_7
        fields = ('docfile','visible')
        widgets = {
            'docfile': forms.FileInput({'id': 'fileway7'}),
        }

class JuryAuth(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'username': forms.TextInput({'placeholder': 'Логин', 'id': '21285'}),
            'password': forms.PasswordInput({'placeholder': 'Пароль'}),
        }