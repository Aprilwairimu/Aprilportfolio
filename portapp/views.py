from django.shortcuts import render,redirect
from django.http import HttpRequest,Http404
from urllib import request

# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')