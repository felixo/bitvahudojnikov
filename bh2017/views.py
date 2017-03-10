#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import (HttpResponse, HttpResponseForbidden,
                         HttpResponseRedirect)
from django.core.urlresolvers import reverse
from models import Artist
from forms import ArtistForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def index(request):
    form = ArtistForm()
    return render(request, 'bh2017/index.html', {'form': form})

def thankyou(request):
    return render(request, 'bh2017/thankyou.html')

def addArtist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES)
        if form.is_valid():
            password1 = User.objects.make_random_password()
            user = User.objects.create_user(form.data['email'], form.data['email'], password1)
            profile = form.save(commit=False)
            if profile.user_id is None:
                profile.user_id = user.id
                message = "Поздравляем! Вы успешно зарегестрировались на сайте проекта Битва художников! Ваш пароль: " + password1
            profile.save()
            send_mail(
                'Registration',
                message,
                'robot@bitvahudojnikov.ru',
                [form.data['email']],
                fail_silently=False,
            )
            return HttpResponseRedirect(reverse('bh2017:thankyou'))
    else:
        form = ArtistForm()
    return render(request, 'bh2017/index.html', {'form': form})

@csrf_exempt
def mailCheck(request):
    print "ok"
    email = request.POST.get('email')
    data = True
    if User.objects.filter(username=email).exists():
        data = False
    return HttpResponse(data)