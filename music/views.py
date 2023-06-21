from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
#from music.models import Question,exam_user
from music.models import music_user
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
import random
def greeting(request):
    return render(request,"music/greeting.html")
def signup(request):
    return render(request,"music/signup.html")
def savedata(request):
    if request.method=='POST':
        formData=request.POST
        cre1=User()
        cre=music_user()
        cre1.username=formData['username']
        cre1.set_password(formData['password'])
        cre1.save()
        cre.real_name=formData['name']
        cre.user=cre1
        cre.save()
        request.session['username']=formData['username']
        return  HttpResponseRedirect('http://localhost:8000/music/file/')
def userLogin(request):
    data={}
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            request.session['username']=username
            return  HttpResponseRedirect('http://localhost:8000/music/file/')
        else:
            data['error']="Username or Password is incorrect"
            return render(request,'music/user_login.html',data)
    else:
        return render(request,'music/user_login.html',data)
def userLogout(request):
    logout(request)
    return HttpResponseRedirect('http://localhost:8000/music/login/')

def file(request):
    if 'username' not in request.session:
        return HttpResponseRedirect('http://localhost:8000/music/login/')
    res=render(request,'music/file.html')
    return res
def public_file(request):
    res = render(request,'music/public_file.html')
    return res
def success(request):
    res = render(request,'music/success.html')
    return res
def about(request):
    res = render(request,'music/about.html')
    return res
def contact(request):
    res = render(request,'music/contact.html')
    return res
