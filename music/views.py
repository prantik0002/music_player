from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
#from music.models import Question,exam_user
from music.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
import random
def greeting(request):
    return render(request,"music/greeting.html")
def signup(request):
    return render(request,"music/signup.html")
def savedata4(request):
    if request.method == 'POST':
        email1 = request.POST['email1']
        email2 = request.POST['email2']
        email3 = request.POST['email3']
        
        en1 = User.objects.filter(email=email1)
        en2 = User.objects.filter(email=email2)
        en3 = User.objects.filter(email=email3)
        if en1 in User.objects.all():
            file_name = request.POST['file_name']
            u = User.objects.get(email=email1)
            cre = protected_file_name()
            cre.user = u
            cre.file_name = file_name
            cre.save()
            return HttpResponseRedirect('http://localhost:8000/music/success/')
        if en2 in User.objects.all():
            file_name = request.POST['file_name']
            u = User.objects.get(email=email1)
            cre = protected_file_name()
            cre.user = u
            cre.file_name = file_name
            cre.save()
            return HttpResponseRedirect('http://localhost:8000/music/success/')
        if en3 in User.objects.all():
            file_name = request.POST['file_name']
            u = User.objects.get(email=email1)
            cre = protected_file_name()
            cre.user = u
            cre.file_name = file_name
            cre.save()
            return HttpResponseRedirect('http://localhost:8000/music/success/')

def savedata3(request):
     
    if request.method == 'POST':
        email = request.POST['email']
        file_name = request.POST['file_name']
        u = User.objects.get(email = email)
        cre = private_file_name()
        cre.user = u
        cre.file_name = file_name
        cre.save()
        return HttpResponseRedirect('http://localhost:8000/music/success/')


def savedata2(request):
    if 'email' not in request.session:
        return HttpResponseRedirect('http://localhost:8000/music/login/') 
    if request.method == 'POST':
        result = request.POST['choice']
        print(result)
        if result == '1':
            return  HttpResponseRedirect('http://localhost:8000/music/dashboard/')
        if result == '2':
            return  HttpResponseRedirect('http://localhost:8000/music/private/')
        if result == '3':
            return  HttpResponseRedirect('http://localhost:8000/music/protected/')





def savedata1(request):
    if request.method == 'POST':
        formData = request.POST
        cre = public()
        cre.file_name = formData['file_name']
        
        cre.save()
        
        return  HttpResponseRedirect('http://localhost:8000/music/success/')
        
def dashboard(request):
    if 'email' not in request.session:
        return HttpResponseRedirect('http://localhost:8000/music/login/') 
    records = public.objects.all()
    email = request.session['email']
    u = User.objects.get(email = email)
    records1 = private_file_name.objects.filter(user = u)
    records2 = protected_file_name.objects.filter(user = u)
    
    d={
        'records':records, 
        'records1':records1,
        'records2':records2,   
    }
    return render(request,'music/dashboard.html',d)

def savedata(request):
    if request.method=='POST':
        formData=request.POST
        cre1=User()
        
        cre1.username=formData['username']
        cre1.set_password(formData['password'])
        
        cre1.email=formData['email']
        
        cre1.save()
        request.session['email']=formData['email']
        request.session['username']=formData['username']
        request.session['password']=formData['password']
        return  HttpResponseRedirect('http://localhost:8000/music/choice/')
def userLogin(request):
    data={}
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        email = request.POST['email']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            request.session['email']=email
            request.session['username']=username
            request.session['password']=password
            return  HttpResponseRedirect('http://localhost:8000/music/choice/')
        else:
            data['error']="Username or Password is incorrect"
            return render(request,'music/user_login.html',data)
    else:
        return render(request,'music/user_login.html',data)
def userLogout(request):
    logout(request)
    return HttpResponseRedirect('http://localhost:8000/music/login/')
def choice(request):
    return render(request,'music/choice.html')

def file(request):
    if 'username' not in request.session:
        return HttpResponseRedirect('http://localhost:8000/music/login/')
    res=render(request,'music/file.html')
    return res
def public_file(request):
    res = render(request,'music/public_file.html')
    return res
def private_file(request):
    res = render(request,'music/private.html')
    return res
def protected_file(request):
    res = render(request,'music/protected.html')
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
