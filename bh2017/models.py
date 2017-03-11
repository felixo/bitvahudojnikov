#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models
from datetime import datetime



Status = (
    ('Unseen', 'На рассмотрении'),
    ('Approved', 'Утверждено'),
    ('Denide', 'Отклонено'),
)

class Artist(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=70)
    city = models.CharField(max_length=200)
    favorite = models.CharField(max_length=200, choices=Status)
    data = models.DateTimeField('date published', auto_now_add=True)

    def __unicode__(self):  # __unicode__ on Python 2
        return unicode(self.name) or u''

class Jury(models.Model):
    name = models.CharField(max_length=200)
    user = models.OneToOneField(User)

    def __unicode__(self):  # __unicode__ on Python 2
        return unicode(self.name) or u''

class Tasks(models.Model):
    name = models.CharField(max_length=200)
    text = models.CharField(max_length=2000)

    def __unicode__(self):  # __unicode__ on Python 2
        return unicode(self.art_host_name) or u''

class Faq(models.Model):
    quest = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)

    def __unicode__(self):  # __unicode__ on Python 2
        return unicode(self.art_host_name) or u''

class Partner(models.Model):
    name = models.CharField(max_length=200)
    text = models.CharField(max_length=2000)
    logo = models.FileField(upload_to='logoPartner')

    def __unicode__(self):  # __unicode__ on Python 2
        return unicode(self.name) or u''

class Sponsor(models.Model):
    name = models.CharField(max_length=200)
    text = models.CharField(max_length=2000)
    logo = models.FileField(upload_to='logoSponsor')

    def __unicode__(self):  # __unicode__ on Python 2
        return unicode(self.art) or u''

class Task_1(models.Model):
    art = models.ForeignKey(Artist, on_delete=models.CASCADE)
    docfile = models.FileField(upload_to='Task1')
    visible = models.BooleanField(default=False)
    data = models.DateTimeField('date published', auto_now_add=True)

class Task_2(models.Model):
    art = models.ForeignKey(Artist, on_delete=models.CASCADE)
    docfile = models.FileField(upload_to='Task2')
    visible = models.BooleanField(default=False)
    data = models.DateTimeField('date published', auto_now_add=True)

class Task_3(models.Model):
    art = models.ForeignKey(Artist, on_delete=models.CASCADE)
    docfile = models.FileField(upload_to='Task4')
    visible = models.BooleanField(default=False)
    data = models.DateTimeField('date published', auto_now_add=True)

class Task_4(models.Model):
    art = models.ForeignKey(Artist, on_delete=models.CASCADE)
    docfile = models.FileField(upload_to='Task4')
    visible = models.BooleanField(default=False)
    data = models.DateTimeField('date published', auto_now_add=True)

class Task_5(models.Model):
    art = models.ForeignKey(Artist, on_delete=models.CASCADE)
    docfile = models.FileField(upload_to='Task5')
    visible = models.BooleanField(default=False)
    data = models.DateTimeField('date published', auto_now_add=True)

class Task_6(models.Model):
    art = models.ForeignKey(Artist, on_delete=models.CASCADE)
    docfile = models.FileField(upload_to='Task6')
    visible = models.BooleanField(default=False)
    data = models.DateTimeField('date published', auto_now_add=True)

class Task_7(models.Model):
    art = models.ForeignKey(Artist, on_delete=models.CASCADE)
    docfile = models.FileField(upload_to='Task7')
    visible = models.BooleanField(default=False)
    data = models.DateTimeField('date published', auto_now_add=True)

class Vote(models.Model):
    art = models.ForeignKey(Artist, on_delete=models.CASCADE)
    vote_id = models.ForeignKey(User, related_name='votes')
    vote_is_it = models.BooleanField(default=False)
    data = models.DateTimeField('date published', auto_now_add=True)

    def __unicode__(self):  # __unicode__ on Python 2
        return unicode(self.art) or u''
