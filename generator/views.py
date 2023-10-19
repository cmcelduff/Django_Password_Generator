from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generatorapp/home.html')

def about(request):
    return render(request, 'generatorapp/about.html')

def password(request):

    Characters = list('abcdefghijklmnopqrstuvwxyz')

    length = int(request.GET.get('length',12))

    if request.GET.get('uppercase'):
        Characters.extend(list('ACBDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        Characters.extend(list('!"£$%^&*()_-=+{}[]:;@~#<>,./?|\`¬'))
    if request.GET.get('numbers'):
        Characters.extend(list('1234567890'))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(Characters)

    return render(request, 'generatorapp/password.html', {'password':thepassword})