from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the BITVA HUDOJNIKOV 2017 index.")