from django.shortcuts import render,redirect
from django.http import HttpRequest,Http404
from urllib import request
from .models import *
import requests,json
# Create your views here.


def home(request):
    return render(request,'home.html')
   

def about(request):
    return render(request, 'about.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def resume(request):
    return render(request, 'resume.html')

def testimonials(request):
    return render(request, 'testimonials.html')

def contact(request):
    return render(request, 'contact.html')