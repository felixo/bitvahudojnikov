from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'bh2017/index.html')