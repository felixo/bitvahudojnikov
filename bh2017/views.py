#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import (HttpResponse, HttpResponseForbidden,
                         HttpResponseRedirect)
from django.core.urlresolvers import reverse
from models import Artist, Partner
from forms import ArtistForm, UserAuth
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate,login, logout


def index(request):
    form = ArtistForm()
    formAuth = UserAuth()
    obj = Partner.objects.all()
    paginator = Paginator(obj, 12)
    page = request.GET.get('page')
    print request.user
    fullName = 0
    if (request.user.is_authenticated):
        fullName = Artist.objects.filter(user=request.user)
        fullName = fullName[0].name
    try:
        documents = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        documents = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        documents = paginator.page(paginator.num_pages)
    return render(request, 'bh2017/index.html', {'form': form, 'documents': documents, 'formAuth': formAuth, 'Artist': fullName})

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

def registration(request):
    return render(request, 'bh2017/registration.html')

def tasks(request):
    return render(request, 'bh2017/tasks.html')

def prizes(request):
    return render(request, 'bh2017/prizes.html')

def rules(request):
    return render(request, 'bh2017/rules.html')

def jury(request):
    return render(request, 'bh2017/jury.html')

def sponsors(request):
    return render(request, 'bh2017/sponsors.html')

def partners(request):
    return render(request, 'bh2017/partners.html')

def faq(request):
    return render(request, 'bh2017/faq.html')

def forgetpass(request):
    return render(request, 'bh2017/forgetpass.html')

def loginAuth(request):
    if request.method == 'POST':
        formAuth = UserAuth(request.POST, request.FILES)
        if formAuth.is_valid():
            user = authenticate(username=formAuth.data['email'], password=formAuth.data['password'])
            if user is not None:
                login(request, user)
            # A backend authenticated the credentials
                print 'OK'
                return HttpResponseRedirect(reverse('bh2017:index'))
            else:
            # No backend authenticated the credentials
                print 'Nope'
                data = "0"
            return HttpResponseRedirect(reverse('bh2017:loginFail'))
  #  else:
 #       form = ArtistForm()
 #   return render(request, 'bh2017/index.html', {'form': form})

def logoutArtist(request):
    logout(request)
    #return HttpResponse("shit")
    return HttpResponseRedirect(reverse('bh2017:index'))

def loginFail(request):
    formAuth = UserAuth()
    obj = Partner.objects.all()
    paginator = Paginator(obj, 12)
    page = request.GET.get('page')
    print request.user
    fullName = 0
    if (request.user.is_authenticated):
        fullName = Artist.objects.filter(user=request.user)
        fullName = fullName[0].name
    try:
        documents = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        documents = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        documents = paginator.page(paginator.num_pages)
    return render(request, 'bh2017/loginFail.html', {'documents': documents, 'formAuth': formAuth, 'Artist': fullName})