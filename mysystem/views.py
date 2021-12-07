from django.shortcuts import render, redirect
from django.http import Http404
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt

from mysystem.models import *
from django.contrib.auth import login, logout, authenticate
from mysystem.models import course, Cornellstu, anouncement, attendence
import datetime


# Create your views here.


def home(request):
    return render(request, 'index.html')

@csrf_exempt
def admin_login(request):
    error = False
    if request.method == "POST":
        u = request.POST.get('username')
        p = request.POST.get('password')
        print(u)
        print(p)
        user = authenticate(request, username=u, password=p)
        if user:
            login(request, user)
            return redirect('home')
        else:
            error = True
    d = {'error': error}
    return render(request, 'login.html', d)


def viewcourse(request, id):
    # if not request.user.is_authenticated:
    #         return redirect('home')
    data = Cornellstu.objects.filter(netid=id)
    print(data.courseinfo.time1)
    print(data.courseinfo.time2)
    print(data.courseinfo.time3)


def viewattendence(request):
    # if not request.user.is_authenticated:
    #         return redirect('home')
    order = attendence.objects.first()
    a = []

    print(order.stu1)

    d = {'data1': order}
    return render(request, 'attend.html', d)


def viewAnnouncement(request):
    if not request.user.is_authenticated:
        return redirect('home')
    data = anouncement.objects.first()
    print(data.content)
    return render(request, 'index.html')


def announce(request):
    # if not request.user.is_authenticated:
    #     return redirect('home')
    error3 = False

    if request.method == "POST":
        c = request.POST['content']
        t = request.Post['title']
        anouncement.objects.create(time='2021-12-13', title=t, content=c)

    return render(request, 'announce.html')


def admin_logout(request):
    # logout(request)
    return render(request, 'logout.html')

# def Signup(request):
#     error=False
#     error1=False
#     if request.method == "POST":
#         f=request.POST['firstname']
#         l=request.POST['lastname']
#         n=request.POST['netid']
#         u=request.POST['username']
#         p=request.POST['password']
#         e=request.POST['email']
#         user = User.objects.filter(username = u)
#         if user:
#             error= True
#         else:
#             us = User.objects.create_user(username=u,password=p, first_name=f,last_name=l )
#             error1=True
#     d = {"error":error,'error1':error1}
#     return render(request,'Signup.html',d)