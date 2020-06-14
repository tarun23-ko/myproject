from django.shortcuts import render
from django.http import HttpResponse
import time
from django.contrib.auth.models import User
# Create your views here.
def Start(request):

  return render(request,"Membership/Registration.html")

def Register(request):
  return render(request,"Membership/signup.html")

def TEMPLOGIN(request):


  return render(request,"Membership/Tempindex.html")
def open(request):
  return render(request,"Membership/index.html")
def login(request):
  return render(request,"Membership/login.html")

def handlesignup(request):
  if request.method=="POST":
    firstname=request.POST['firstname']
    lastname = request.POST['lastname']
    email=request.POST['email']
    password = request.POST['password']
    phone = request.POST['phone']


