from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import (
    DateField, DateTimeField, DurationField, Field, IntegerField, TimeField,
)
# Create your models here.



class AutoUser(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.TextField()
    email = models.TextField()
    birth = models.DateTimeField()
    high_school = models.CharField(max_length = 30, null = True, blank = True, default = '고등학교를 입력하세요')
    university = models.CharField(max_length = 30, null = True, blank = True, default = '대학교를 입력하세요')
    major = models.TextField(null = True)
    profile = models.ImageField(null=True, blank=True)



class License(models.Model):
    user = models.ForeignKey(AutoUser, on_delete = models.CASCADE)
    title = models.TextField()
    score = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_achieved = models.DateTimeField()
    upload_image = models.ImageField(null=True, blank=True)
    upload_file = models.FileField(upload_to="%Y/%m/%d")

class Intern(models.Model):
    user = models.ForeignKey(AutoUser, on_delete= models.CASCADE, related_name = 'intern')
    title = models.TextField()
    summary = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField()
    upload_image = models.ImageField(null=True, blank=True)
    upload_file = models.FileField(upload_to='uploads/%Y/%m/%d/')

class Paper(models.Model):
    user = models.ForeignKey(AutoUser, on_delete= models.CASCADE, related_name = 'paper')
    title = models.TextField()
    summary = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    upload_file = models.FileField(upload_to='uploads/%Y/%m/%d/')

class Other(models.Model):
    title = models.TextField()
    summary = models.TextField()
    upload_image = models.ImageField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    upload_file = models.FileField(upload_to='uploads/%Y/%m/%d/')