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
        attr