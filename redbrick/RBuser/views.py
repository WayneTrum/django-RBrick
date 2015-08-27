from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import auth 

# Create your views here.

def home(request):
  user = request.user
  if request.method == 'GET':
    return render(request,'home.html',{'is_login':user})

def login(request):
  if request.method == 'GET':
    return render(request,'login.html')
  elif request.method == 'POST':
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    userforname = auth.authenticate(username=username,password=password)
    if userforname is not None and userforname.is_active:
      auth.login(request,userforname)
      return redirect('/home')
    else:
      userforemail = auth.authenticate(email=username,password=password)
      if userforemail is not None and userforemail.is_active:
        auth.login(request,userforemail)
        return redirect('/home')
      else:
        return render(request,'login.html')

def register(request):
  if request.method == 'GET':
    return render(request,'register.html')
  elif request.method == 'POST':
    username = request.POST.get('username','')
    email = request.POST.get('email','')
    password = request.POST.get('password','')
    userfind = User.objects.filter(Q(username=username) | Q(email=username))
    if userfind is None:
      user = User.objects.create_user(username,email,password)
      user.is_staff = True
      user.save()
      return redirect('/home')
    else:
      return redirect('/register')

def loginout(request):
  auth.logout(request)
  return redirect('/home')