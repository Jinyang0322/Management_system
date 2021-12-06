from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class anouncement(models.Model):
    time = models.CharField(max_length=50, null=True)
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


    def __str__(self):
        return self.name
