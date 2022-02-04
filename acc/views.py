from email import message
from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.contrib.auth.hashers import check_password
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, "acc/index.html")

def login_user(request):
    if request.method =="POST":
        un = request.POST.get("uname")
        pw = request.POST.get("upass")
        user = authenticate(username=un, password=pw)
        if user:
            login(request, user)
            messages.success(request, f"{user} 님 환영합니다!!!")
            return redirect("acc:index")
        else:
            messages.error(request, "Login Fail!!!")
    return render(request, "acc/login.html")

def logout_user(request):
    logout(request)
    return redirect("acc:login")

def signup(request):
    if request.method == "POST":
        un = request.POST.get("name")
        pw = request.POST.get("password")
        ag = request.POST.get("age")
        com = request.POST.get("comment")
        img = request.FILES.get("image") #사진 파일 넣을 때
        User.objects.create_user(username=un,password=pw, age=ag, comment=com, pic=img)
        return redirect("acc:login")
    return render(request,"acc/signup.html")

def profile(request):
    return render(request, "acc/profile.html")

def delete(request):
    if check_password(request.POST.get("passcheck"),request.user.password):
        #비밀번호 체크, 일치하면 True 일치하지 않으면 False
        request.user.delete()
    return redirect("acc:index")

def update(request):
    if request.method =="POST":
        u = request.user
        npw = request.POST.get("npass")
        nc = request.POST.get("ncom")
        npic = request.FILES.get("npic")
        #User.objects.
        if npw:
            u.set_password(npw)#비밀번호 재설정
        if npic:
            u.pic.delete()
            u.pic = npic#사진 재설정
        u.comment = nc
        u.save()
        login(request, u)
        return redirect("acc:profile")
    return render(request, "acc/update.html")