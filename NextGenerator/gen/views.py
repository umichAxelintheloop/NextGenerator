from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def home(request):
    return render(request, 'gen/home.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvxyz')

    if request.GET.get('Uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!"#$%&/()=?/*-+-_.,:;{[@^}]'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    length = int(request.GET.get('lenght', 12))

    thePassword = ''

    for x in range(length):

        thePassword += random.choice(characters)

    return render(request, 'gen/password.html', {'password':thePassword})

def about(request):
    return render(request, 'gen/about.html')