#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import (HttpResponse, HttpResponseForbidden,
                         HttpResponseRedirect)
from django.core.urlresolvers import reverse
from models import Artist, Partner, Jury, Tasks, Task_1, Task_6, Task_7, Task_3, Task_5, Task_2, Task_4, Vote
from forms import ArtistForm, UserAuth, registrationFull, changePersonal, passwordChange, forgetPass, loadArt1, loadArt2, loadArt3, loadArt4, loadArt5, loadArt6, loadArt7, JuryAuth
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate,login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

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
            try:
                user = User.objects.create_user(form.data['email'], form.data['email'], password1)
            except IntegrityError:
                return HttpResponseRedirect(reverse('bh2017:message'))
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
    formAuth = UserAuth()
    obj = Partner.objects.all()
    paginator = Paginator(obj, 12)
    page = request.GET.get('page')
    fullName = None
    loadArt_1 = loadArt1()
    loadArt_2 = loadArt2()
    loadArt_3 = loadArt3()
    loadArt_4 = loadArt4()
    loadArt_5 = loadArt5()
    loadArt_6 = loadArt6()
    loadArt_7 = loadArt7()
    tasks1 = None
    task_1 = None
    task_2 = None
    task_3 = None
    task_4 = None
    task_5 = None
    task_6 = None
    task_7 = None
    if not request.user.is_anonymous():
        fullName = Artist.objects.filter(user=request.user)
        fullName = fullName[0].name
    	tasks1 = Tasks.objects.all()
    	task_1 = Task_1.objects.filter(artist1=request.user)
    	task_2 = Task_2.objects.filter(artist1=request.user)
    	task_3 = Task_3.objects.filter(artist1=request.user)
    	task_4 = Task_4.objects.filter(artist1=request.user)
    	task_5 = Task_5.objects.filter(artist1=request.user)
    	task_6 = Task_6.objects.filter(artist1=request.user)
    	task_7 = Task_7.objects.filter(artist1=request.user)
    #print task_1
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
    return render(request, 'bh2017/tasks.html', {'documents': documents, 'formAuth': formAuth, 'Artist': fullName, 'tasks': tasks1, 'task_1': task_1, 'task_2': task_2, 'task_3': task_3, 'task_4': task_4, 'task_5': task_5, 'task_6': task_6, 'task_7': task_7, 'loadArt_1': loadArt_1, 'loadArt_2': loadArt_2, 'loadArt_3': loadArt_3, 'loadArt_4': loadArt_4, 'loadArt_5': loadArt_5, 'loadArt_6': loadArt_6, 'loadArt_7': loadArt_7})

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
    jurys = Jury.objects.all()
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
    return render(request, 'bh2017/jury.html', {'documents': documents, 'formAuth': formAuth, 'Artist': fullName, 'jurys': jurys})

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
            try:
                user = User.objects.create_user(form.data['email'], form.data['email'], password1)
            except IntegrityError:
                return HttpResponseRedirect(reverse('bh2017:message'))
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
    forgetPassForm = forgetPass(initial={'age': 'Ваш возраст'})
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
                return HttpResponseRedirect(reverse('bh2017:errorpass'))
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
                print "here3"
                return HttpResponseRedirect(reverse('bh2017:errorpass'))
        else:
            return HttpResponseRedirect(reverse('bh2017:errorpass'))

def errorpass(request):
    forgetPassForm = forgetPass(initial={'age': 'Ваш возраст'})
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

def message(request):
    formAuth = UserAuth()
    obj = Partner.objects.all()
    paginator = Paginator(obj, 12)
    page = request.GET.get('page')
    regForm = registrationFull(initial={'age': 'Ваш возраст'})
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
    return render(request, 'bh2017/message.html', {'documents': documents, 'formAuth': formAuth, 'Artist': fullName, 'regForm': regForm})

@csrf_exempt
def loadmorepartner(request):
    obj = Partner.objects.all()
    paginator = Paginator(obj, 12)
    page = request.GET.get('page')
    data = ''
    try:
        documents = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        documents = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        documents = paginator.page(paginator.num_pages)
    for document in documents:
        data = data + '<li class="partnerDot"><a href="'+document.text+'" class="partnerLinks"><img id="document.id" src="'+document.logo.url+'" alt="Reducto!" class="partnerLogo"></a></li>'
    next = documents.has_next()
    print next
    if next:
        data = data + '///?page=' + str(documents.next_page_number())
    else:
        data = data + '///Last'
    return HttpResponse(data)

def loadImg1(request):
    if request.method == 'POST':
        form = loadArt1(request.POST, request.FILES)
        if form.is_valid():
            task_1 = Task_1(artist1=request.user, docfile=request.FILES['docfile'], visible=True)
            task_1.save()
            return HttpResponseRedirect(reverse('bh2017:tasks'))
    else:
        form = ArtistForm()
    return render(request, 'bh2017/index.html', {'form': form})

def deleteImg1(request):
    if request.method == 'POST':
        Task_1.objects.filter(artist1=request.user).delete()
        return HttpResponseRedirect(reverse('bh2017:tasks'))

def loadImg1(request):
    if request.method == 'POST':
        form = loadArt1(request.POST, request.FILES)
        if form.is_valid():
            task_1 = Task_1(artist1=request.user, docfile=request.FILES['docfile'], visible=True)
            task_1.save()
            return HttpResponseRedirect(reverse('bh2017:tasks'))
    else:
        form = ArtistForm()
    return render(request, 'bh2017/index.html', {'form': form})

def deleteImg1(request):
    if request.method == 'POST':
        Task_1.objects.filter(artist1=request.user).delete()
        return HttpResponseRedirect(reverse('bh2017:tasks'))

def loadImg2(request):
    if request.method == 'POST':
        form = loadArt2(request.POST, request.FILES)
        if form.is_valid():
            task_2 = Task_2(artist1=request.user, docfile=request.FILES['docfile'], visible=True)
            task_2.save()
            return HttpResponseRedirect(reverse('bh2017:tasks'))
    else:
        form = ArtistForm()
    return render(request, 'bh2017/index.html', {'form': form})

def deleteImg2(request):
    if request.method == 'POST':
        Task_2.objects.filter(artist1=request.user).delete()
        return HttpResponseRedirect(reverse('bh2017:tasks'))

def loadImg3(request):
    if request.method == 'POST':
        form = loadArt3(request.POST, request.FILES)
        if form.is_valid():
            task_3 = Task_3(artist1=request.user, docfile=request.FILES['docfile'], visible=True)
            task_3.save()
            return HttpResponseRedirect(reverse('bh2017:tasks'))
    else:
        form = ArtistForm()
    return render(request, 'bh2017/index.html', {'form': form})

def deleteImg3(request):
    if request.method == 'POST':
        Task_3.objects.filter(artist1=request.user).delete()
        return HttpResponseRedirect(reverse('bh2017:tasks'))

def loadImg4(request):
    if request.method == 'POST':
        form = loadArt4(request.POST, request.FILES)
        if form.is_valid():
            task_4 = Task_4(artist1=request.user, docfile=request.FILES['docfile'], visible=True)
            task_4.save()
            return HttpResponseRedirect(reverse('bh2017:tasks'))
    else:
        form = ArtistForm()
    return render(request, 'bh2017/index.html', {'form': form})

def deleteImg4(request):
    if request.method == 'POST':
        Task_4.objects.filter(artist1=request.user).delete()
        return HttpResponseRedirect(reverse('bh2017:tasks'))

def loadImg5(request):
    if request.method == 'POST':
        form = loadArt5(request.POST, request.FILES)
        if form.is_valid():
            task_5 = Task_5(artist1=request.user, docfile=request.FILES['docfile'], visible=True)
            task_5.save()
            return HttpResponseRedirect(reverse('bh2017:tasks'))
    else:
        form = ArtistForm()
    return render(request, 'bh2017/index.html', {'form': form})

def deleteImg5(request):
    if request.method == 'POST':
        Task_5.objects.filter(artist1=request.user).delete()
        return HttpResponseRedirect(reverse('bh2017:tasks'))

def loadImg6(request):
    if request.method == 'POST':
        form = loadArt6(request.POST, request.FILES)
        if form.is_valid():
            task_6 = Task_6(artist1=request.user, docfile=request.FILES['docfile'], visible=True)
            task_6.save()
            return HttpResponseRedirect(reverse('bh2017:tasks'))
    else:
        form = ArtistForm()
    return render(request, 'bh2017/index.html', {'form': form})

def deleteImg6(request):
    if request.method == 'POST':
        Task_6.objects.filter(artist1=request.user).delete()
        return HttpResponseRedirect(reverse('bh2017:tasks'))

def loadImg7(request):
    if request.method == 'POST':
        form = loadArt7(request.POST, request.FILES)
        if form.is_valid():
            task_7 = Task_7(artist1=request.user, docfile=request.FILES['docfile'], visible=True)
            task_7.save()
            return HttpResponseRedirect(reverse('bh2017:tasks'))
    else:
        form = ArtistForm()
    return render(request, 'bh2017/index.html', {'form': form})

def deleteImg7(request):
    if request.method == 'POST':
        Task_7.objects.filter(artist1=request.user).delete()
        return HttpResponseRedirect(reverse('bh2017:tasks'))

def loginJury(request):
    juryAuth = JuryAuth()
    fullName = None
    if not request.user.is_anonymous():
        try:
            fullName = Jury.objects.filter(user=request.user)
            fullName = fullName[0].name
        except IndexError:
            fullName = None
            logout(request)
    return render(request, 'bh2017/loginJury.html', {'juryAuth': juryAuth, 'Artist': fullName})

def AuthJury(request):
    if request.method == 'POST':
        juryAuth = JuryAuth(data=request.POST)
        user = authenticate(username=juryAuth.data['username'], password=juryAuth.data['password'])
        if user is not None:
            login(request, user)
            print 'OK'
            return HttpResponseRedirect(reverse('bh2017:loginJury'))
        else:
            print 'Nope'
            data = "0"
            return HttpResponseRedirect(reverse('bh2017:loginJury'))
    print 'whats wrong with you'
    return HttpResponseRedirect(reverse('bh2017:loginJury'))

@login_required
def gallery1(request):
    juryAuth = JuryAuth()
    fullName = None
    obj = Task_1.objects.all()
    paginator = Paginator(obj, 6)
    page = request.GET.get('page')
    votes = Vote.objects.filter(vote_id=request.user)
    try:
        documents = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        documents = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        documents = paginator.page(paginator.num_pages)
    if not request.user.is_anonymous():
        try:
            fullName = Jury.objects.filter(user=request.user)
            fullName = fullName[0].name
        except IndexError:
            fullName = None
            logout(request)
    listOfTrue = []
    for document in documents:
        if votes.filter(paint_1=document.id):
            listOfTrue.append(True)
        else:
            listOfTrue.append(False)
    listOfTrue = zip(documents, listOfTrue)
    return  render(request, 'bh2017/gallery1.html', {'documents': documents,'juryAuth': juryAuth, 'Artist': fullName, 'votes': votes, 'listOfTrue': listOfTrue})

def vote1(request, paint_id):
    if not request.user.is_anonymous():
        try:
            vote_is_it = Vote.objects.filter(vote_id=request.user).filter(paint_1=paint_id)[0].vote_is_it
        except IndexError:
            vote_is_it = False
        if vote_is_it:
            Vote.objects.filter(vote_id=request.user).filter(paint_1=paint_id).delete()
            obj = Task_1.objects.filter(id=paint_id)[0]
            obj.count = obj.count - 1
            obj.save()
        else:
            return HttpResponseRedirect(reverse('bh2017:loginJury'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def remVote1(request, paint_id):
    if not request.user.is_anonymous():
        try:
            vote_is_it = Vote.objects.filter(vote_id=request.user).filter(paint_1=paint_id)[0].vote_is_it
        except IndexError:
            vote_is_it = False
        if vote_is_it:
            return HttpResponseRedirect(reverse('bh2017:loginJury'))
        else:
            print Jury.objects.filter(user=request.user)
            obj = Task_1.objects.filter(id=paint_id)[0]
            obj.count = obj.count + 1
            obj.save()
            vote = Vote.objects.create(vote_id=request.user, paint_1=obj, vote_is_it=True)
            vote.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseRedirect(reverse('bh2017:loginJury'))

@login_required
def gallery2(request):
    juryAuth = JuryAuth()
    fullName = None
    obj = Task_2.objects.all()
    paginator = Paginator(obj, 6)
    page = request.GET.get('page')
    votes = Vote.objects.filter(vote_id=request.user)
    try:
        documents = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        documents = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        documents = paginator.page(paginator.num_pages)
    if not request.user.is_anonymous():
        try:
            fullName = Jury.objects.filter(user=request.user)
            fullName = fullName[0].name
        except IndexError:
            fullName = None
            logout(request)
    listOfTrue = []
    for document in documents:
        if votes.filter(paint_2=document.id):
            listOfTrue.append(True)
        else:
            listOfTrue.append(False)
    listOfTrue = zip(documents, listOfTrue)
    return  render(request, 'bh2017/gallery2.html', {'documents': documents,'juryAuth': juryAuth, 'Artist': fullName, 'votes': votes, 'listOfTrue': listOfTrue})

def vote2(request, paint_id):
    if not request.user.is_anonymous():
        try:
            vote_is_it = Vote.objects.filter(vote_id=request.user).filter(paint_2=paint_id)[0].vote_is_it
        except IndexError:
            vote_is_it = False
        if vote_is_it:
            Vote.objects.filter(vote_id=request.user).filter(paint_2=paint_id).delete()
            obj = Task_2.objects.filter(id=paint_id)[0]
            obj.count = obj.count - 1
            obj.save()
        else:
            return HttpResponseRedirect(reverse('bh2017:loginJury'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def remVote2(request, paint_id):
    if not request.user.is_anonymous():
        try:
            vote_is_it = Vote.objects.filter(vote_id=request.user).filter(paint_2=paint_id)[0].vote_is_it
        except IndexError:
            vote_is_it = False
        if vote_is_it:
            return HttpResponseRedirect(reverse('bh2017:loginJury'))
        else:
            print Jury.objects.filter(user=request.user)
            obj = Task_2.objects.filter(id=paint_id)[0]
            obj.count = obj.count + 1
            obj.save()
            vote = Vote.objects.create(vote_id=request.user, paint_2=obj, vote_is_it=True)
            vote.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseRedirect(reverse('bh2017:loginJury'))

@login_required
def gallery3(request):
    juryAuth = JuryAuth()
    fullName = None
    obj = Task_3.objects.all()
    paginator = Paginator(obj, 6)
    page = request.GET.get('page')
    votes = Vote.objects.filter(vote_id=request.user)
    try:
        documents = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        documents = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        documents = paginator.page(paginator.num_pages)
    if not request.user.is_anonymous():
        try:
            fullName = Jury.objects.filter(user=request.user)
            fullName = fullName[0].name
        except IndexError:
            fullName = None
            logout(request)
    listOfTrue = []
    for document in documents:
        if votes.filter(paint_3=document.id):
            listOfTrue.append(True)
        else:
            listOfTrue.append(False)
    listOfTrue = zip(documents, listOfTrue)
    return  render(request, 'bh2017/gallery3.html', {'documents': documents,'juryAuth': juryAuth, 'Artist': fullName, 'votes': votes, 'listOfTrue': listOfTrue})

def vote3(request, paint_id):
    if not request.user.is_anonymous():
        try:
            vote_is_it = Vote.objects.filter(vote_id=request.user).filter(paint_3=paint_id)[0].vote_is_it
        except IndexError:
            vote_is_it = False
        if vote_is_it:
            Vote.objects.filter(vote_id=request.user).filter(paint_3=paint_id).delete()
            obj = Task_3.objects.filter(id=paint_id)[0]
            obj.count = obj.count - 1
            obj.save()
        else:
            return HttpResponseRedirect(reverse('bh2017:loginJury'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def remVote3(request, paint_id):
    if not request.user.is_anonymous():
        try:
            vote_is_it = Vote.objects.filter(vote_id=request.user).filter(paint_3=paint_id)[0].vote_is_it
        except IndexError:
            vote_is_it = False
        if vote_is_it:
            return HttpResponseRedirect(reverse('bh2017:loginJury'))
        else:
            print Jury.objects.filter(user=request.user)
            obj = Task_3.objects.filter(id=paint_id)[0]
            obj.count = obj.count + 1
            obj.save()
            vote = Vote.objects.create(vote_id=request.user, paint_3=obj, vote_is_it=True)
            vote.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseRedirect(reverse('bh2017:loginJury'))

@login_required
def gallery4(request):
    juryAuth = JuryAuth()
    fullName = None
    obj = Task_4.objects.all()
    paginator = Paginator(obj, 6)
    page = request.GET.get('page')
    votes = Vote.objects.filter(vote_id=request.user)
    try:
        documents = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        documents = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        documents = paginator.page(paginator.num_pages)
    if not request.user.is_anonymous():
        try:
            fullName = Jury.objects.filter(user=request.user)
            fullName = fullName[0].name
        except IndexError:
            fullName = None
            logout(request)
    listOfTrue = []
    for document in documents:
        if votes.filter(paint_4=document.id):
            listOfTrue.append(True)
        else:
            listOfTrue.append(False)
    listOfTrue = zip(documents, listOfTrue)
    return  render(request, 'bh2017/gallery4.html', {'documents': documents,'juryAuth': juryAuth, 'Artist': fullName, 'votes': votes, 'listOfTrue': listOfTrue})

def vote4(request, paint_id):
    if not request.user.is_anonymous():
        try:
            vote_is_it = Vote.objects.filter(vote_id=request.user).filter(paint_4=paint_id)[0].vote_is_it
        except IndexError:
            vote_is_it = False
        if vote_is_it:
            Vote.objects.filter(vote_id=request.user).filter(paint_4=paint_id).delete()
            obj = Task_4.objects.filter(id=paint_id)[0]
            obj.count = obj.count - 1
            obj.save()
        else:
            return HttpResponseRedirect(reverse('bh2017:loginJury'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def remVote4(request, paint_id):
    if not request.user.is_anonymous():
        try:
            vote_is_it = Vote.objects.filter(vote_id=request.user).filter(paint_4=paint_id)[0].vote_is_it
        except IndexError:
            vote_is_it = False
        if vote_is_it:
            return HttpResponseRedirect(reverse('bh2017:loginJury'))
        else:
            print Jury.objects.filter(user=request.user)
            obj = Task_4.objects.filter(id=paint_id)[0]
            obj.count = obj.count + 1
            obj.save()
            vote = Vote.objects.create(vote_id=request.user, paint_4=obj, vote_is_it=True)
            vote.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseRedirect(reverse('bh2017:loginJury'))

@login_required
def gallery5(request):
    juryAuth = JuryAuth()
    fullName = None
    obj = Task_5.objects.all()
    paginator = Paginator(obj, 6)
    page = request.GET.get('page')
    votes = Vote.objects.filter(vote_id=request.user)
    try:
        documents = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        documents = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        documents = paginator.page(paginator.num_pages)
    if not request.user.is_anonymous():
        try:
            fullName = Jury.objects.filter(user=request.user)
            fullName = fullName[0].name
        except IndexError:
            fullName = None
            logout(request)
    listOfTrue = []
    for document in documents:
        if votes.filter(paint_5=document.id):
            listOfTrue.append(True)
        else:
            listOfTrue.append(False)
    listOfTrue = zip(documents, listOfTrue)
    return  render(request, 'bh2017/gallery5.html', {'documents': documents,'juryAuth': juryAuth, 'Artist': fullName, 'votes': votes, 'listOfTrue': listOfTrue})

def vote5(request, paint_id):
    if not request.user.is_anonymous():
        try:
            vote_is_it = Vote.objects.filter(vote_id=request.user).filter(paint_5=paint_id)[0].vote_is_it
        except IndexError:
            vote_is_it = False
        if vote_is_it:
            Vote.objects.filter(vote_id=request.user).filter(paint_5=paint_id).delete()
            obj = Task_5.objects.filter(id=paint_id)[0]
            obj.count = obj.count - 1
            obj.save()
        else:
            return HttpResponseRedirect(reverse('bh2017:loginJury'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def remVote5(request, paint_id):
    if not request.user.is_anonymous():
        try:
            vote_is_it = Vote.objects.filter(vote_id=request.user).filter(paint_5=paint_id)[0].vote_is_it
        except IndexError:
            vote_is_it = False
        if vote_is_it:
            return HttpResponseRedirect(reverse('bh2017:loginJury'))
        else:
            print Jury.objects.filter(user=request.user)
            obj = Task_5.objects.filter(id=paint_id)[0]
            obj.count = obj.count + 1
            obj.save()
            vote = Vote.objects.create(vote_id=request.user, paint_5=obj, vote_is_it=True)
            vote.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseRedirect(reverse('bh2017:loginJury'))

@login_required
def gallery6(request):
    juryAuth = JuryAuth()
    fullName = None
    obj = Task_6.objects.all()
    paginator = Paginator(obj, 6)
    page = request.GET.get('page')
    votes = Vote.objects.filter(vote_id=request.user)
    try:
        documents = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        documents = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        documents = paginator.page(paginator.num_pages)
    if not request.user.is_anonymous():
        try:
            fullName = Jury.objects.filter(user=request.user)
            fullName = fullName[0].name
        except IndexError:
            fullName = None
            logout(request)
    listOfTrue = []
    for document in documents:
        if votes.filter(paint_6=document.id):
            listOfTrue.append(True)
        else:
            listOfTrue.append(False)
    listOfTrue = zip(documents, listOfTrue)
    return  render(request, 'bh2017/gallery6.html', {'documents': documents,'juryAuth': juryAuth, 'Artist': fullName, 'votes': votes, 'listOfTrue': listOfTrue})

def vote6(request, paint_id):
    if not request.user.is_anonymous():
        try:
            vote_is_it = Vote.objects.filter(vote_id=request.user).filter(paint_6=paint_id)[0].vote_is_it
        except IndexError:
            vote_is_it = False
        if vote_is_it:
            Vote.objects.filter(vote_id=request.user).filter(paint_6=paint_id).delete()
            obj = Task_6.objects.filter(id=paint_id)[0]
            obj.count = obj.count - 1
            obj.save()
        else:
            return HttpResponseRedirect(reverse('bh2017:loginJury'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def remVote6(request, paint_id):
    if not request.user.is_anonymous():
        try:
            vote_is_it = Vote.objects.filter(vote_id=request.user).filter(paint_6=paint_id)[0].vote_is_it
        except IndexError:
            vote_is_it = False
        if vote_is_it:
            return HttpResponseRedirect(reverse('bh2017:loginJury'))
        else:
            print Jury.objects.filter(user=request.user)
            obj = Task_6.objects.filter(id=paint_id)[0]
            obj.count = obj.count + 1
            obj.save()
            vote = Vote.objects.create(vote_id=request.user, paint_6=obj, vote_is_it=True)
            vote.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseRedirect(reverse('bh2017:loginJury'))

login_required
def gallery7(request):
    juryAuth = JuryAuth()
    fullName = None
    obj = Task_7.objects.all()
    paginator = Paginator(obj, 6)
    page = request.GET.get('page')
    votes = Vote.objects.filter(vote_id=request.user)
    try:
        documents = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        documents = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        documents = paginator.page(paginator.num_pages)
    if not request.user.is_anonymous():
        try:
            fullName = Jury.objects.filter(user=request.user)
            fullName = fullName[0].name
        except IndexError:
            fullName = None
            logout(request)
    listOfTrue = []
    for document in documents:
        if votes.filter(paint_7=document.id):
            listOfTrue.append(True)
        else:
            listOfTrue.append(False)
    listOfTrue = zip(documents, listOfTrue)
    return  render(request, 'bh2017/gallery7.html', {'documents': documents,'juryAuth': juryAuth, 'Artist': fullName, 'votes': votes, 'listOfTrue': listOfTrue})

def vote7(request, paint_id):
    if not request.user.is_anonymous():
        try:
            vote_is_it = Vote.objects.filter(vote_id=request.user).filter(paint_7=paint_id)[0].vote_is_it
        except IndexError:
            vote_is_it = False
        if vote_is_it:
            Vote.objects.filter(vote_id=request.user).filter(paint_7=paint_id).delete()
            obj = Task_7.objects.filter(id=paint_id)[0]
            obj.count = obj.count - 1
            obj.save()
        else:
            return HttpResponseRedirect(reverse('bh2017:loginJury'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def remVote7(request, paint_id):
    if not request.user.is_anonymous():
        try:
            vote_is_it = Vote.objects.filter(vote_id=request.user).filter(paint_7=paint_id)[0].vote_is_it
        except IndexError:
            vote_is_it = False
        if vote_is_it:
            return HttpResponseRedirect(reverse('bh2017:loginJury'))
        else:
            print Jury.objects.filter(user=request.user)
            obj = Task_7.objects.filter(id=paint_id)[0]
            obj.count = obj.count + 1
            obj.save()
            vote = Vote.objects.create(vote_id=request.user, paint_7=obj, vote_is_it=True)
            vote.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseRedirect(reverse('bh2017:loginJury'))

def com_gallerys(request):
    formAuth = UserAuth()
    fullName = None
    if not request.user.is_anonymous():
        try:
            fullName = Artist.objects.filter(user=request.user)
            fullName = fullName[0].name
        except IndexError:
            fullName = None
            logout(request)
    return render(request, 'bh2017/com_gallerys.html', {'juryAuth': formAuth, 'Artist': fullName})

def login_gallerys(request):
    if request.method == 'POST':
        formAuth = UserAuth(request.POST, request.FILES)
        if formAuth.is_valid():
            user = authenticate(username=formAuth.data['email'], password=formAuth.data['password'])
            if user is not None:
                login(request, user)
            # A backend authenticated the credentials
                print 'OK'
                return HttpResponseRedirect(reverse('bh2017:com_gallerys'))
            else:
            # No backend authenticated the credentials
                print 'Nope'
                data = "0"
            return HttpResponseRedirect(reverse('bh2017:loginFail'))
    return HttpResponseRedirect(reverse('bh2017:loginFail'))

@login_required
def com_gallery1(request):
    juryAuth = UserAuth()
    fullName = None
    obj = Task_1.objects.all()
    paginator = Paginator(obj, 6)
    page = request.GET.get('page')
    votes = Vote.objects.filter(vote_id=request.user)
    try:
        documents = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        documents = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        documents = paginator.page(paginator.num_pages)
    if not request.user.is_anonymous():
        try:
            fullName = Artist.objects.filter(user=request.user)
            fullName = fullName[0].name
        except IndexError:
            fullName = None
            logout(request)
    listOfTrue = []
    for document in documents:
        if votes.filter(paint_1=document.id):
            listOfTrue.append(True)
        else:
            listOfTrue.append(False)
    listOfTrue = zip(documents, listOfTrue)
    return  render(request, 'bh2017/com_gallery1.html', {'documents': documents,'juryAuth': juryAuth, 'Artist': fullName, 'votes': votes, 'listOfTrue': listOfTrue})

@login_required
def com_gallery2(request):
    juryAuth = UserAuth()
    fullName = None
    obj = Task_2.objects.all()
    paginator = Paginator(obj, 6)
    page = request.GET.get('page')
    votes = Vote.objects.filter(vote_id=request.user)
    try:
        documents = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        documents = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        documents = paginator.page(paginator.num_pages)
    if not request.user.is_anonymous():
        try:
            fullName = Artist.objects.filter(user=request.user)
            fullName = fullName[0].name
        except IndexError:
            fullName = None
            logout(request)
    listOfTrue = []
    for document in documents:
        if votes.filter(paint_2=document.id):
            listOfTrue.append(True)
        else:
            listOfTrue.append(False)
    listOfTrue = zip(documents, listOfTrue)
    return  render(request, 'bh2017/com_gallery2.html', {'documents': documents,'juryAuth': juryAuth, 'Artist': fullName, 'votes': votes, 'listOfTrue': listOfTrue})

@login_required
def com_gallery3(request):
    juryAuth = UserAuth()
    fullName = None
    obj = Task_3.objects.all()
    paginator = Paginator(obj, 6)
    page = request.GET.get('page')
    votes = Vote.objects.filter(vote_id=request.user)
    try:
        documents = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        documents = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        documents = paginator.page(paginator.num_pages)
    if not request.user.is_anonymous():
        try:
            fullName = Artist.objects.filter(user=request.user)
            fullName = fullName[0].name
        except IndexError:
            fullName = None
            logout(request)
    listOfTrue = []
    for document in documents:
        if votes.filter(paint_3=document.id):
            listOfTrue.append(True)
        else:
            listOfTrue.append(False)
    listOfTrue = zip(documents, listOfTrue)
    return  render(request, 'bh2017/com_gallery3.html', {'documents': documents,'juryAuth': juryAuth, 'Artist': fullName, 'votes': votes, 'listOfTrue': listOfTrue})

@login_required
def com_gallery4(request):
    juryAuth = UserAuth()
    fullName = None
    obj = Task_4.objects.all()
    paginator = Paginator(obj, 6)
    page = request.GET.get('page')
    votes = Vote.objects.filter(vote_id=request.user)
    try:
        documents = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        documents = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        documents = paginator.page(paginator.num_pages)
    if not request.user.is_anonymous():
        try:
            fullName = Artist.objects.filter(user=request.user)
            fullName = fullName[0].name
        except IndexError:
            fullName = None
            logout(request)
    listOfTrue = []
    for document in documents:
        if votes.filter(paint_4=document.id):
            listOfTrue.append(True)
        else:
            listOfTrue.append(False)
    listOfTrue = zip(documents, listOfTrue)
    return  render(request, 'bh2017/com_gallery4.html', {'documents': documents,'juryAuth': juryAuth, 'Artist': fullName, 'votes': votes, 'listOfTrue': listOfTrue})

@login_required
def com_gallery5(request):
    juryAuth = UserAuth()
    fullName = None
    obj = Task_5.objects.all()
    paginator = Paginator(obj, 6)
    page = request.GET.get('page')
    votes = Vote.objects.filter(vote_id=request.user)
    try:
        documents = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        documents = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        documents = paginator.page(paginator.num_pages)
    if not request.user.is_anonymous():
        try:
            fullName = Artist.objects.filter(user=request.user)
            fullName = fullName[0].name
        except IndexError:
            fullName = None
            logout(request)
    listOfTrue = []
    for document in documents:
        if votes.filter(paint_5=document.id):
            listOfTrue.append(True)
        else:
            listOfTrue.append(False)
    listOfTrue = zip(documents, listOfTrue)
    return  render(request, 'bh2017/com_gallery5.html', {'documents': documents,'juryAuth': juryAuth, 'Artist': fullName, 'votes': votes, 'listOfTrue': listOfTrue})

@login_required
def com_gallery6(request):
    juryAuth = UserAuth()
    fullName = None
    obj = Task_6.objects.all()
    paginator = Paginator(obj, 6)
    page = request.GET.get('page')
    votes = Vote.objects.filter(vote_id=request.user)
    try:
        documents = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        documents = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        documents = paginator.page(paginator.num_pages)
    if not request.user.is_anonymous():
        try:
            fullName = Artist.objects.filter(user=request.user)
            fullName = fullName[0].name
        except IndexError:
            fullName = None
            logout(request)
    listOfTrue = []
    for document in documents:
        if votes.filter(paint_6=document.id):
            listOfTrue.append(True)
        else:
            listOfTrue.append(False)
    listOfTrue = zip(documents, listOfTrue)
    return  render(request, 'bh2017/com_gallery6.html', {'documents': documents,'juryAuth': juryAuth, 'Artist': fullName, 'votes': votes, 'listOfTrue': listOfTrue})

@login_required
def com_gallery7(request):
    juryAuth = UserAuth()
    fullName = None
    obj = Task_7.objects.all()
    paginator = Paginator(obj, 6)
    page = request.GET.get('page')
    votes = Vote.objects.filter(vote_id=request.user)
    try:
        documents = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        documents = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        documents = paginator.page(paginator.num_pages)
    if not request.user.is_anonymous():
        try:
            fullName = Artist.objects.filter(user=request.user)
            fullName = fullName[0].name
        except IndexError:
            fullName = None
            logout(request)
    listOfTrue = []
    for document in documents:
        if votes.filter(paint_7=document.id):
            listOfTrue.append(True)
        else:
            listOfTrue.append(False)
    listOfTrue = zip(documents, listOfTrue)
    return  render(request, 'bh2017/com_gallery7.html', {'documents': documents,'juryAuth': juryAuth, 'Artist': fullName, 'votes': votes, 'listOfTrue': listOfTrue})


def com_vote1(request, paint_id):
    if not request.user.is_anonymous():
        try:
            vote_is_it = Vote.objects.filter(vote_id=request.user).filter(paint_1=paint_id)[0].vote_is_it
        except IndexError:
            vote_is_it = False
        if vote_is_it:
            Vote.objects.filter(vote_id=request.user).filter(paint_1=paint_id).delete()
            obj = Task_1.objects.filter(id=paint_id)[0]
            obj.com_count = obj.com_count - 1
            obj.save()
        else:
            return HttpResponseRedirect(reverse('bh2017:com_gallerys'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def com_remVote1(request, paint_id):
    if not request.user.is_anonymous():
        try:
            vote_is_it = Vote.objects.filter(vote_id=request.user).filter(paint_1=paint_id)[0].vote_is_it
        except IndexError:
            vote_is_it = False
        if vote_is_it:
            return HttpResponseRedirect(reverse('bh2017:com_gallerys'))
        else:
            print Jury.objects.filter(user=request.user)
            obj = Task_1.objects.filter(id=paint_id)[0]
            obj.com_count = obj.com_count + 1
            obj.save()
            vote = Vote.objects.create(vote_id=request.user, paint_1=obj, vote_is_it=True)
            vote.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseRedirect(reverse('bh2017:com_gallerys'))


def com_vote2(request, paint_id):
    if not request.user.is_anonymous():
        try:
            vote_is_it = Vote.objects.filter(vote_id=request.user).filter(paint_2=paint_id)[0].vote_is_it
        except IndexError:
            vote_is_it = False
        if vote_is_it:
            Vote.objects.filter(vote_id=request.user).filter(paint_2=paint_id).delete()
            obj = Task_2.objects.filter(id=paint_id)[0]
            obj.com_count = obj.com_count - 1
            obj.save()
        else:
            return HttpResponseRedirect(reverse('bh2017:com_gallerys'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def com_remVote2(request, paint_id):
    if not request.user.is_anonymous():
        try:
            vote_is_it = Vote.objects.filter(vote_id=request.user).filter(paint_2=paint_id)[0].vote_is_it
        except IndexError:
            vote_is_it = False
        if vote_is_it:
            return HttpResponseRedirect(reverse('bh2017:com_gallerys'))
        else:
            print Jury.objects.filter(user=request.user)
            obj = Task_2.objects.filter(id=paint_id)[0]
            obj.com_count = obj.com_count + 1
            obj.save()
            vote = Vote.objects.create(vote_id=request.user, paint_2=obj, vote_is_it=True)
            vote.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseRedirect(reverse('bh2017:com_gallerys'))


def com_vote3(request, paint_id):
    if not request.user.is_anonymous():
        try:
            vote_is_it = Vote.objects.filter(vote_id=request.user).filter(paint_3=paint_id)[0].vote_is_it
        except IndexError:
            vote_is_it = False
        if vote_is_it:
            Vote.objects.filter(vote_id=request.user).filter(paint_3=paint_id).delete()
            obj = Task_3.objects.filter(id=paint_id)[0]
            obj.com_count = obj.com_count - 1
            obj.save()
        else:
            return HttpResponseRedirect(reverse('bh2017:com_gallerys'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def com_remVote3(request, paint_id):
    if not request.user.is_anonymous():
        try:
            vote_is_it = Vote.objects.filter(vote_id=request.user).filter(paint_3=paint_id)[0].vote_is_it
        except IndexError:
            vote_is_it = False
        if vote_is_it:
            return HttpResponseRedirect(reverse('bh2017:com_gallerys'))
        else:
            print Jury.objects.filter(user=request.user)
            obj = Task_3.objects.filter(id=paint_id)[0]
            obj.com_count = obj.com_count + 1
            obj.save()
            vote = Vote.objects.create(vote_id=request.user, paint_3=obj, vote_is_it=True)
            vote.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseRedirect(reverse('bh2017:com_gallerys'))


def com_vote4(request, paint_id):
    if not request.user.is_anonymous():
        try:
            vote_is_it = Vote.objects.filter(vote_id=request.user).filter(paint_4=paint_id)[0].vote_is_it
        except IndexError:
            vote_is_it = False
        if vote_is_it:
            Vote.objects.filter(vote_id=request.user).filter(paint_4=paint_id).delete()
            obj = Task_4.objects.filter(id=paint_id)[0]
            obj.com_count = obj.com_count - 1
            obj.save()
        else:
            return HttpResponseRedirect(reverse('bh2017:com_gallerys'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def com_remVote4(request, paint_id):
    if not request.user.is_anonymous():
        try:
            vote_is_it = Vote.objects.filter(vote_id=request.user).filter(paint_4=paint_id)[0].vote_is_it
        except IndexError:
            vote_is_it = False
        if vote_is_it:
            return HttpResponseRedirect(reverse('bh2017:com_gallerys'))
        else:
            print Jury.objects.filter(user=request.user)
            obj = Task_4.objects.filter(id=paint_id)[0]
            obj.com_count = obj.com_count + 1
            obj.save()
            vote = Vote.objects.create(vote_id=request.user, paint_4=obj, vote_is_it=True)
            vote.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseRedirect(reverse('bh2017:com_gallerys'))


def com_vote5(request, paint_id):
    if not request.user.is_anonymous():
        try:
            vote_is_it = Vote.objects.filter(vote_id=request.user).filter(paint_5=paint_id)[0].vote_is_it
        except IndexError:
            vote_is_it = False
        if vote_is_it:
            Vote.objects.filter(vote_id=request.user).filter(paint_5=paint_id).delete()
            obj = Task_5.objects.filter(id=paint_id)[0]
            obj.com_count = obj.com_count - 1
            obj.save()
        else:
            return HttpResponseRedirect(reverse('bh2017:com_gallerys'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def com_remVote5(request, paint_id):
    if not request.user.is_anonymous():
        try:
            vote_is_it = Vote.objects.filter(vote_id=request.user).filter(paint_5=paint_id)[0].vote_is_it
        except IndexError:
            vote_is_it = False
        if vote_is_it:
            return HttpResponseRedirect(reverse('bh2017:com_gallerys'))
        else:
            print Jury.objects.filter(user=request.user)
            obj = Task_5.objects.filter(id=paint_id)[0]
            obj.com_count = obj.com_count + 1
            obj.save()
            vote = Vote.objects.create(vote_id=request.user, paint_5=obj, vote_is_it=True)
            vote.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseRedirect(reverse('bh2017:com_gallerys'))


def com_vote6(request, paint_id):
    if not request.user.is_anonymous():
        try:
            vote_is_it = Vote.objects.filter(vote_id=request.user).filter(paint_6=paint_id)[0].vote_is_it
        except IndexError:
            vote_is_it = False
        if vote_is_it:
            Vote.objects.filter(vote_id=request.user).filter(paint_6=paint_id).delete()
            obj = Task_6.objects.filter(id=paint_id)[0]
            obj.com_count = obj.com_count - 1
            obj.save()
        else:
            return HttpResponseRedirect(reverse('bh2017:com_gallerys'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def com_remVote6(request, paint_id):
    if not request.user.is_anonymous():
        try:
            vote_is_it = Vote.objects.filter(vote_id=request.user).filter(paint_6=paint_id)[0].vote_is_it
        except IndexError:
            vote_is_it = False
        if vote_is_it:
            return HttpResponseRedirect(reverse('bh2017:com_gallerys'))
        else:
            print Jury.objects.filter(user=request.user)
            obj = Task_6.objects.filter(id=paint_id)[0]
            obj.com_count = obj.com_count + 1
            obj.save()
            vote = Vote.objects.create(vote_id=request.user, paint_6=obj, vote_is_it=True)
            vote.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseRedirect(reverse('bh2017:com_gallerys'))


def com_vote7(request, paint_id):
    if not request.user.is_anonymous():
        try:
            vote_is_it = Vote.objects.filter(vote_id=request.user).filter(paint_7=paint_id)[0].vote_is_it
        except IndexError:
            vote_is_it = False
        if vote_is_it:
            Vote.objects.filter(vote_id=request.user).filter(paint_7=paint_id).delete()
            obj = Task_7.objects.filter(id=paint_id)[0]
            obj.com_count = obj.com_count - 1
            obj.save()
        else:
            return HttpResponseRedirect(reverse('bh2017:com_gallerys'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def com_remVote7(request, paint_id):
    if not request.user.is_anonymous():
        try:
            vote_is_it = Vote.objects.filter(vote_id=request.user).filter(paint_7=paint_id)[0].vote_is_it
        except IndexError:
            vote_is_it = False
        if vote_is_it:
            return HttpResponseRedirect(reverse('bh2017:com_gallerys'))
        else:
            print Jury.objects.filter(user=request.user)
            obj = Task_7.objects.filter(id=paint_id)[0]
            obj.com_count = obj.com_count + 1
            obj.save()
            vote = Vote.objects.create(vote_id=request.user, paint_7=obj, vote_is_it=True)
            vote.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseRedirect(reverse('bh2017:com_gallerys'))

