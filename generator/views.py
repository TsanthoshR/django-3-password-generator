from django.shortcuts import render
from django.http import HttpResponse
import random





# Create your views here.

def hello(request):
    return HttpResponse('hello world')

def eggs(request):
    return HttpResponse('<h1>1. Scrambled Eggs</h1>')

def home(request):
    return render(request,'generator/home.html',{'pass':'ityfcfct878'})

def password(request):
    characters=list('abcdefghijklmnopqrstuvwxyz')
    length=int(request.GET.get('length',default=12))
    thepassword=""

    if request.GET.get('Uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('Numbers'):
        characters.extend(list('0123456789'))
    if request.GET.get('Special_Characters'):
        characters.extend(list('!@#$%^&*()'))

    for x in range(length):
        thepassword += random.choice(characters)
    return render(request,'generator/password.html',{'password':thepassword})

def about(request):
    return render(request,'generator/about.html')
