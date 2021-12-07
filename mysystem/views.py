from django.shortcuts import render, redirect,HttpResponse
from django.http import Http404, JsonResponse
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from datetime import date

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
        json_result = json.loads(postBody)
        u = json_result['username']
        p = json_result['password']
        user = authenticate(request, username=u, password=p)
        error = True
        j = json.dumps(error)
        d = {'result': j}
        # return render(request, 'login.html', d)
        return JsonResponse({'status':'ok'})
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

    # data1 = Cornellstu.objects.filter(netid=id)
    # filter()返回的是QuerySet,相当于做了一次筛选，而不是返回一条实例
    data = Cornellstu.objects.get(netid=id)
    a = {'t1':data.courseinfo.time1, 't2':data.courseinfo.time2, 't3':data.courseinfo.time3}
    return JsonResponse(a)

@csrf_exempt
def viewattendence(request):
    # if not request.user.is_authenticated:
    #         return redirect('home')
    if request.method == "POST":
        order = attendence.objects.first()
        a = {'1': order.stu1, '2': order.stu2, '3': order.stu3, '4': order.stu4, '5': order.stu5, '6': order.stu6,
             '7': order.stu7, '8': order.stu8, '9': order.stu9, '10': order.stu10 }
        d = {'data1': order}
        return JsonResponse(a)
    return render(request, 'attend.html')


def viewAnnouncement(request):
    # if not request.user.is_authenticated:
    #     return redirect('home')
    data = anouncement.objects.last()
    a = {'time': data.time, 'title': data.title, 'content': data.content}
    return JsonResponse(a)


@csrf_exempt
def announce(request):
    # if not request.user.is_authenticated:
    #     return redirect('home')
    error3 = False

    if request.method == "POST":

        postBody = request.body
        json_result = json.loads(postBody)
        c = json_result['content']
        t = json_result['title']

        anouncement.objects.create(time=date.today, title=t, content=c)
        return JsonResponse({'status':'ok'})

    return render(request, 'announce.html')


def admin_logout(request):
    # logout(request)
    return render(request, 'logout.html')


# def index1(request):
#     if request.method=="POST":
#         username = request.POST.get("username")
#         pwd = request.POST.get("password")
#
#         print(username)
#         print(pwd)
#
#         if username == "klvchen" and pwd=="123":
#             return HttpResponse("登录成功")
#     #return render(req, "login.html")
#     kl = "you are welcome"
#     a = "hello"
#     b = "world"
#     c = "what"
#     return render_to_response("index1.html", locals())

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