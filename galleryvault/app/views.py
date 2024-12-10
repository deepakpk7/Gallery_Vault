from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import *
import os
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

from django.http import HttpResponse


# Create your views here.
# username:demo@gmail.com
# password:demo

def user_login(req):
    if 'user' in req.session:
        return redirect(index)
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['password']
        data=authenticate(username=uname,password=password)
        if data:
            login(req,data)
            if data.is_superuser:
                req.session['shop']=uname  #Create Session
                return redirect(index)
            else:
                req.session['user']=uname
                return redirect(index)
        else:
            messages.warning(req, "Invalid Username or Password")
            return redirect(user_login)
    else:
        return render(req,'login.html')
    
def register(req):
    if req.method=='POST':
        uname=req.POST['uname']
        email=req.POST['email']
        pswd=req.POST['pswd']
        # send_mail('Eshop Registration', 'EShop account created sucssfully', settings.EMAIL_HOST_USER, [email])

        try:
            data=User.objects.create_user(first_name=uname,email=email,
                                        username=email,password=pswd)
            data.save()
        except:
            messages.warning(req, "Username or Email already exist")
            return redirect(register)
        return redirect(user_login)
    else:
        return render(req,'register.html')
    
def index(req):
    if 'user' in req.session:
        data=UploadedFile.objects.all()
        return render(req,'index.html',{'file':data})
    else:
        return redirect(user_login)
    
def upload(req):
    if 'user' in req.session:
        print(req.FILES)  
        if 'imges' in req.FILES:
            img=req.FILES['imges']
            data=UploadedFile.objects.create(file=img)
            data.save()
        else:
            print("File key 'imges' not found in req.FILES")
    return render(req, "upload.html")

def file_delete(req,pid):
    if 'user' in req.session:
        data=UploadedFile.objects.filter(pk=pid)
        data.delete()
        return redirect(index)

def user_logout(req):
    logout(req)
    req.session.flush() #Delete session
    return redirect(user_login)