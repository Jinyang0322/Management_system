from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class anouncement(models.Model):
    time = models.DateField(default=date.today)
    title = models.CharField(max_length=100, null=True)
    content = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.title


class course(models.Model):
    time1 = models.CharField(max_length=100, null=True)
    time2 = models.CharField(max_length=100, null=True)
    time3 = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.title


class Cornellstu(models.Model):
    courseinfo = models.ForeignKey(course, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True)
    absences = models.IntegerField(null=True)
    netid = models.CharField(max_length=50, null=True)


    def __str__(self):
        return self.name

class attendence(models.Model):

    stu1 = models.BooleanField(default=False)
    stu2 = models.BooleanField(default=False)
    stu3 = models.BooleanField(default=False)
    stu4 = models.BooleanField(default=False)
    stu5 = models.BooleanField(default=False)
    stu6 = models.BooleanField(default=False)
    stu7 = models.BooleanField(default=False)
    stu8 = models.BooleanField(default=False)
    stu9 = models.BooleanField(default=False)
    stu10 = models.BooleanField(default=False)


class Surveytable(models.Model):
    description = models.CharField(max_length=100, null=True)
    question1 = models.CharField(max_length=100, null=True)



class Surveyresult(models.Model):
    ans1 = models.BooleanField(default=False)
    ans2 = models.BooleanField(default=False)
    ans3 = models.BooleanField(default=False)
    ans4 = models.BooleanField(default=False)
    ans5 = models.BooleanField(default=False)
    ans6 = models.BooleanField(default=False)
    ans7 = models.BooleanField(default=False)
    ans8 = models.BooleanField(default=False)
    ans9 = models.BooleanField(default=False)
    ans10 = models.BooleanField(default=False)






