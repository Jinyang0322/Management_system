from django.shortcuts import render, redirect,HttpResponse,render_to_response
from django.http import Http404
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt

from mysystem.models import *
from django.contrib.auth import login, logout, authenticate
from mysystem.models import course, Cornellstu, anouncement, attendence
import datetime
import json


# Create your views here.


def home(request):
    return render(request, 'index.html')

@csrf_exempt
def admin_login(request):
    error = False
    if request.method == "POST":
        postBody = request.body
        print(type(postBody))
        print(postBody)
        json_result = json.loads(postBody)
        u = json_result['username']
        p = json_result['password']
        print(u)
        print(p)
        user = authenticate(request, username=u, password=p)
        error = True
        j = json.dumps(error)
        d = {'result': j}
        # return render(request, 'login.html', d)
        return HttpResponse("login success")
        # if user:
        #     login(request, user)
        #     return redirect('home')
        # else:
        #     error = True
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


def index1(request):
    if request.method=="POST":
        username = request.POST.get("username")
        pwd = request.POST.get("password")

        print(username)
        print(pwd)

        if username == "klvchen" and pwd=="123":
            return HttpResponse("登录成功")
    #return render(req, "login.html")
    kl = "you are welcome"
    a = "hello"
    b = "world"
    c = "what"
    return render_to_response("index1.html", locals())

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