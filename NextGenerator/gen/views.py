from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def home(request):
    return render(request, 'gen/home.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvxyz')

    length = int(request.GET.get('lenght'))

    thePassword = ''

    for x in range(length):

        thePassword += random.choice(characters)

    return render(request, 'gen/password.html', {'password':thePassword})