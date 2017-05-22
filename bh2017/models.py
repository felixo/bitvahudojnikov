#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models
from datetime import datetime
from tinymce.models import HTMLField


Status = (
    ('','Любимый инструмент'),
    ('akvarek', 'Акварельные краски'),
    ('akril', 'Акриловые краски'),
    ('oil', 'Масляные краски'),
    ('akp', 'Капиллярные ручки'),
    ('color', 'Цветные карандаши'),
    ('mono', 'Монохромные инструменты'),

)

class Artist(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(max_length=70)
    city = models.CharField(max_length=200)
    favorite = models.CharField(max_length=200, choices=Status)
    data = models.DateTimeField('date published', auto_now_add=True)
    age = models.IntegerField(default=0);
    count_of_task = models.IntegerField(default=0, verbose_name="Выполненых заданий")
    votess = models.IntegerField(default=0, verbose_name="Голоса финалистов")

    def __unicode__(self):  # __unicode__ on Python 2
        return unicode(self.name) or u''

class Jury(models.Model):
    name = models.CharField(max_length=200)
    user = models.OneToOneField(User)
    text = models.CharField(max_length=2000, default="")
    docfile = models.FileField(upload_to='Jurys', default="")
    Post = models.CharField(max_length=2000, default="")
    Post2 = HTMLField(default="")

    def __unicode__(self):  # __unicode__ on Python 2
        return unicode(self.name) or u''

class Tasks(models.Model):
    name = models.CharField(max_length=200)
    text = models.CharField(max_length=2000)
    visible = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __unicode__(self):  # __unicode__ on Python 2
        return unicode(self.name) or u''

class Faq(models.Model):
    quest = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)

    def __unicode__(self):  # __unicode__ on Python 2
        return unicode(self.art_host_name) or u''

class Partner(models.Model):
    name = models.CharField(max_length=200)
    text = models.CharField(max_length=2000)
    logo = models.FileField(upload_to='logoPartner')
    text2 = models.CharField(max_length=2000, default="")

    def __unicode__(self):  # __unicode__ on Python 2
        return unicode(self.name) or u''

class Sponsor(models.Model):
    name = models.CharField(max_length=200)
    text = models.CharField(max_length=2000)
    logo = models.FileField(upload_to='logoSponsor')

    def __unicode__(self):  # __unicode__ on Python 2
        return unicode(self.art) or u''

class Task_1(models.Model):
    artist1 = models.OneToOneField(User, default='', verbose_name="Художник")
    docfile = models.FileField(upload_to='Task1', verbose_name="Рисунок")
    visible = models.BooleanField(default=False)
    data = models.DateTimeField('date published', auto_now_add=True)
    count = models.IntegerField(default=0, verbose_name="Голосов")
    com_count = models.IntegerField(default=0, verbose_name="Симпы")


class Task_2(models.Model):
    artist1 = models.OneToOneField(User, default='', verbose_name="Художник")
    docfile = models.FileField(upload_to='Task2', verbose_name="Рисунок")
    visible = models.BooleanField(default=False)
    data = models.DateTimeField('date published', auto_now_add=True)
    count = models.IntegerField(default=0, verbose_name="Голосов")
    com_count = models.IntegerField(default=0, verbose_name="Симпы")

class Task_3(models.Model):
    artist1 = models.OneToOneField(User, default='', verbose_name="Художник")
    docfile = models.FileField(upload_to='Task4', verbose_name="Рисунок")
    visible = models.BooleanField(default=False)
    data = models.DateTimeField('date published', auto_now_add=True)
    count = models.IntegerField(default=0, verbose_name="Голосов")
    com_count = models.IntegerField(default=0, verbose_name="Симпы")

class Task_4(models.Model):
    artist1 = models.OneToOneField(User, default='', verbose_name="Художник")
    docfile = models.FileField(upload_to='Task4', verbose_name="Рисунок")
    visible = models.BooleanField(default=False)
    data = models.DateTimeField('date published', auto_now_add=True)
    count = models.IntegerField(default=0, verbose_name="Голосов")
    com_count = models.IntegerField(default=0, verbose_name="Симпы")

class Task_5(models.Model):
    artist1 = models.OneToOneField(User, default='', verbose_name="Художник")
    docfile = models.FileField(upload_to='Task5', verbose_name="Рисунок")
    visible = models.BooleanField(default=False)
    data = models.DateTimeField('date published', auto_now_add=True)
    count = models.IntegerField(default=0, verbose_name="Голосов")
    com_count = models.IntegerField(default=0, verbose_name="Симпы")

class Task_6(models.Model):
    artist1 = models.OneToOneField(User, default='', verbose_name="Художник")
    docfile = models.FileField(upload_to='Task6', verbose_name="Рисунок")
    visible = models.BooleanField(default=False)
    data = models.DateTimeField('date published', auto_now_add=True)
    count = models.IntegerField(default=0, verbose_name="Голосов")
    com_count = models.IntegerField(default=0, verbose_name="Симпы")

class Task_7(models.Model):
    artist1 = models.OneToOneField(User, default='', verbose_name="Художник")
    docfile = models.FileField(upload_to='Task7', verbose_name="Рисунок")
    visible = models.BooleanField(default=False)
    data = models.DateTimeField('date published', auto_now_add=True)
    count = models.IntegerField(default=0, verbose_name="Голосов")
    com_count = models.IntegerField(default=0, verbose_name="Симпы")

class Vote(models.Model):
    paint_1 = models.ForeignKey(Task_1, on_delete=models.CASCADE, blank=True, null=True)
    paint_2 = models.ForeignKey(Task_2, on_delete=models.CASCADE, blank=True, null=True)
    paint_3 = models.ForeignKey(Task_3, on_delete=models.CASCADE, blank=True, null=True)
    paint_4 = models.ForeignKey(Task_4, on_delete=models.CASCADE, blank=True, null=True)
    paint_5 = models.ForeignKey(Task_5, on_delete=models.CASCADE, blank=True, null=True)
    paint_6 = models.ForeignKey(Task_6, on_delete=models.CASCADE, blank=True, null=True)
    paint_7 = models.ForeignKey(Task_7, on_delete=models.CASCADE, blank=True, null=True)
    final = models.IntegerField(default=0, verbose_name="Голосов")
    vote_id = models.ForeignKey(User, related_name='votes')
    vote_is_it = models.BooleanField(default=False)
    data = models.DateTimeField('date published', auto_now_add=True)




    def __unicode__(self):  # __unicode__ on Python 2
        return unicode(self.vote_id) or u''

