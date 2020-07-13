from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

# Create your views here.


def destinations(request):
    
    return render(request,'destinations.html')