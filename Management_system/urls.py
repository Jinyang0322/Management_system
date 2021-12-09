"""Management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mysystem.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('index/', home, name='home'),
    path('login/', admin_login, name='login'),
    path('logout/', admin_logout, name='logout'),
    path('viewannounce/', viewAnnouncement, name='viewanounce'),
    path('announce/', announce, name='viewanounce'),
    path('viewcourse/<str:id>', viewcourse, name='viewcourse'),
    path('attend/', viewattendence, name='attendence'),
    path('account/', Signup, name='register'),
    path('count/', count_attend, name='count'),
    path('survey/', survey, name='survey'),
    path('survey/answer/', sendans, name='sendanswer'),
    path('response/', viewresponse, name='response'),
    path('viewquestion/', viewquestion, name='questions'),
    path('test/', viewtest, name='test')



    # path('test/', index1, name = 'test'),

]
