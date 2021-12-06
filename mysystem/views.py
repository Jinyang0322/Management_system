from django.shortcuts import render,redirect
from django.http import Http404
from django.urls import reverse_lazy

from mysystem.models import *
from django.contrib.auth import login, logout, authenticate
from mysystem.models import course, Cornellstu, anouncement
import datetime
# Create your views here.


def home(request):
    return render(request, 'index.html')


def admin_login(request):
    error=False
    if request.method=="POST":
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(request,username=u,password=p)
        if user:
            login(request,user)
            return redirect('home')
        else:
            error=True
    d = {'error': error}
    return render(request, 'login.html', d)


# def anounce(request):
#     if not request.user.is_authenticated:
#         return redirect('home')
#     error3=False
#     data =Book.objects.raw('SELECT * FROM library_book')
#
#     if request.method=="POST":
#         b = request.POST['book']
#         i = request.POST['isbn']
#         a = request.POST['author']
#         c = request.POST['category']
#         q = request.POST['quantity']
#         Book.objects.create(book_name=b, author=a, isbn=i, category=c,quantity=q)
#         error3=True
#         d={'error3':error3,'data':data}
#         return render(request,'bookview.html',d)
#
#     return render(request,'AddBook.html')

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