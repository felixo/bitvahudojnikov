#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import (HttpResponse, HttpResponseForbidden,
                         HttpResponseRedirect)
from django.core.urlresolvers import reverse
from models import Artist, Partner
from forms import ArtistForm, UserAuth, registrationFull, changePersonal, passwordChange, forgetPass
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate,login, logout
from django.core.exceptions import ObjectDoesNotExist

def index(request):
    form = ArtistForm()
    formAuth = UserAuth()
    obj = Partner.objects.all()
    paginator = Paginator(obj, 12)
    page = request.GET.get('page')
    #print request.user
    fullName = 0
    if not request.user.is_anonymous():
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
    form = ArtistForm()
    formAuth = UserAuth()
    obj = Partner.objects.all()
    paginator = Paginator(obj, 12)
    page = request.GET.get('page')
    print request.user
    fullName = 0
    if not request.user.is_anonymous():
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
    return render(request, 'bh2017/thankyou.html', {'form': form, 'documents': documents, 'formAuth': formAuth, 'Artist': fullName})

def addArtist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES)
        if form.is_valid():
            password1 = User.objects.make_random_password()
            user = User.objects.create_user(form.data['email'], form.data['email'], password1)
            form.age=0
            profile = form.save(commit=False)
            if profile.user_id is None:
                profile.user_id = user.id
                message = "Поздравляем! Вы успешно зарегистрировались на сайте проекта Битва художников! Ваш пароль: " + password1
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
    #print "ok"
    email = request.POST.get('email')
    data = True
    if User.objects.filter(username=email).exists():
        data = False
    return HttpResponse(data)

def registration(request):
    formAuth = UserAuth()
    regForm = registrationFull(initial={ 'age': 'Ваш возраст' })
    obj = Partner.objects.all()
    paginator = Paginator(obj, 12)
    page = request.GET.get('page')
    fullName = 0
    if not request.user.is_anonymous():
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
    return render(request, 'bh2017/registration.html', {'documents': documents, 'regForm': regForm, 'formAuth': formAuth, 'Artist': fullName})

def tasks(request):
    obj = Partner.objects.all()
    paginator = Paginator(obj, 12)
    page = request.GET.get('page')
    fullName = 0
    if not request.user.is_anonymous():
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
    return render(request, 'bh2017/tasks.html', {'documents': documents})

def prizes(request):
    formAuth = UserAuth()
    obj = Partner.objects.all()
    paginator = Paginator(obj, 12)
    page = request.GET.get('page')
    # print request.user
    fullName = 0
    if not request.user.is_anonymous():
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
    return render(request, 'bh2017/prizes.html', {'documents': documents, 'formAuth': formAuth, 'Artist': fullName})

def rules(request):
    formAuth = UserAuth()
    obj = Partner.objects.all()
    paginator = Paginator(obj, 12)
    page = request.GET.get('page')
    # print request.user
    fullName = 0
    if not request.user.is_anonymous():
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
    return render(request, 'bh2017/rules.html',{'documents': documents, 'formAuth': formAuth, 'Artist': fullName})

def jury(request):
    formAuth = UserAuth()
    obj = Partner.objects.all()
    paginator = Paginator(obj, 12)
    page = request.GET.get('page')
    # print request.user
    fullName = 0
    if not request.user.is_anonymous():
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
    return render(request, 'bh2017/jury.html', {'documents': documents, 'formAuth': formAuth, 'Artist': fullName})

def sponsors(request):
    formAuth = UserAuth()
    fullName = 0
    if not request.user.is_anonymous():
            fullName = Artist.objects.filter(user=request.user)
            fullName = fullName[0].name
    return render(request, 'bh2017/sponsors.html', {'formAuth': formAuth, 'Artist': fullName})

def partners(request):
    form = ArtistForm()
    formAuth = UserAuth()
    obj = Partner.objects.all()
    fullName = 0
    if not request.user.is_anonymous():
            fullName = Artist.objects.filter(user=request.user)
            fullName = fullName[0].name
    return render(request, 'bh2017/partners.html',{'form': form, 'documents': obj, 'formAuth': formAuth, 'Artist': fullName})

def faq(request):
    formAuth = UserAuth()
    fullName = 0
    if not request.user.is_anonymous():
            fullName = Artist.objects.filter(user=request.user)
            fullName = fullName[0].name
    obj = Partner.objects.all()
    paginator = Paginator(obj, 12)
    page = request.GET.get('page')
    # print request.user
    try:
        documents = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        documents = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        documents = paginator.page(paginator.num_pages)
    return render(request, 'bh2017/faq.html',{'formAuth': formAuth, 'Artist': fullName, 'documents': documents})

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
    if not request.user.is_anonymous():
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

def fullArtistAdd(request):
    if request.method == 'POST':
        form = registrationFull(request.POST, request.FILES)
        if form.is_valid():
            password1 = form.data['password']
            user = User.objects.create_user(form.data['email'], form.data['email'], password1)
            profile = form.save(commit=False)
            if profile.user_id is None:
                profile.user_id = user.id
                message = "Поздравляем! Вы успешно зарегистрировались на сайте проекта Битва художников! Ваш пароль: " + password1
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

def cabinet(request):
    fullName = 0
    if not request.user.is_anonymous():
        fullName = Artist.objects.filter(user=request.user)
	artist = fullName[0]
        fullName = fullName[0].name
    else:
        return HttpResponseRedirect(reverse('bh2017:loginFail'))
    passChange = passwordChange()
    regForm = changePersonal(initial={'name': artist.name, 'city': artist.city, 'age': artist.age, 'favorite': artist.favorite})
    obj = Partner.objects.all()
    paginator = Paginator(obj, 12)
    page = request.GET.get('page')
    try:
        documents = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        documents = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        documents = paginator.page(paginator.num_pages)
    return render(request, 'bh2017/cabinet.html', {'documents': documents, 'Artist': fullName, 'regForm': regForm, 'artist': artist, 'passChange': passChange})

def changeArtist(request):
    if request.method == 'POST':
        form = changePersonal(request.POST, request.FILES)
        fullName = Artist.objects.filter(user=request.user)
        artist = fullName[0]
        if form.is_valid():
            artist.name = form.data['name']
            artist.city = form.data['city']
            artist.age = form.data['age']
            artist.favorite = form.data['favorite']
            artist.save()
            return HttpResponseRedirect(reverse('bh2017:thankyou'))
    else:
        form = ArtistForm()
    return render(request, 'bh2017/index.html', {'form': form})

def changePassword(request):
    if request.method == 'POST':
        form = passwordChange(request.POST, request.FILES)
        if form.is_valid():
            request.user.set_password(form.data['password'])
            request.user.save()
            return HttpResponseRedirect(reverse('bh2017:thankyou'))
    else:
        form = ArtistForm()
    return render(request, 'bh2017/index.html', {'form': form})

def restore(request):
    forgetPassForm = forgetPass()
    formAuth = UserAuth()
    obj = Partner.objects.all()
    paginator = Paginator(obj, 12)
    page = request.GET.get('page')
    if (request.user.is_authenticated):
        return HttpResponseRedirect(reverse('bh2017:index'))
    try:
        documents = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        documents = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        documents = paginator.page(paginator.num_pages)
    return render(request, 'bh2017/forgetPass.html', {'documents': documents,'formAuth': formAuth, 'forgetPassForm': forgetPassForm})

def resetPass(request):
    forgetPassForm = forgetPass()
    formAuth = UserAuth()
    obj = Partner.objects.all()
    paginator = Paginator(obj, 12)
    page = request.GET.get('page')
    if (request.user.is_authenticated):
        return HttpResponseRedirect(reverse('bh2017:index'))
    try:
        documents = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        documents = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        documents = paginator.page(paginator.num_pages)
    if request.method == 'POST':
        form = forgetPass(request.POST, request.FILES)
        if form.is_valid():
            try:
                user = Artist.objects.get(email=form.data['email'])
            except ObjectDoesNotExist:
                return render(request, 'bh2017/restoreError.html', {'documents': documents,'formAuth': formAuth, 'forgetPassForm': forgetPassForm})
            print user.age
            print form.data['age']
            orev = int(form.data['age'])
            if user.age == orev:
                print "here"
                password1 = User.objects.make_random_password()
                print "here"
                user1 = User.objects.get_by_natural_key(username=form.data['email'])
                user1.set_password(password1)
                user1.save()
                message = "Поздравляем! Вы успешно зарегистрировались на сайте проекта Битва художников! Ваш пароль: " + password1
                send_mail(
                    'Registration',
                    message,
                    'robot@bitvahudojnikov.ru',
                    [form.data['email']],
                    fail_silently=False,
                )
                return HttpResponseRedirect(reverse('bh2017:thankyou'))
            else:
                render(request, 'bh2017/restoreError.html',
                       {'documents': documents, 'formAuth': formAuth, 'forgetPassForm': forgetPassForm})
        else:
            return render(request, 'bh2017/restoreError.html', {'documents': documents,'formAuth': formAuth, 'forgetPassForm': forgetPassForm})

def restoreError(request):
    forgetPassForm = forgetPass()
    formAuth = UserAuth()
    obj = Partner.objects.all()
    paginator = Paginator(obj, 12)
    page = request.GET.get('page')
    if (request.user.is_authenticated):
        return HttpResponseRedirect(reverse('bh2017:index'))
    try:
        documents = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        documents = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        documents = paginator.page(paginator.num_pages)
    return render(request, 'bh2017/restoreError.html', {'documents': documents,'formAuth': formAuth, 'forgetPassForm': forgetPassForm})

