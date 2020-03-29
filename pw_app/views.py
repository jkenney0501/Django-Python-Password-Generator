from django.shortcuts import render
from django.http import HttpResponse
import random 


# Create your views here to capture urls request
#primarily functions go here

#this is the home page in the templates --> pwg/home folder
def home(request):
    return render(request, 'pwg/home.html')


#random function to generate random pw
def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length',12))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)
    
    return render(request, 'pwg/password.html', {'password': thepassword })
