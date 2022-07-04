from django.shortcuts import render
from django.http import HttpRequest,Http404
from urllib import request

# Create your views here.


def home(request):
    return render(request, 'home.html')