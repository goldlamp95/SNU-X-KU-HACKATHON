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
    category = models.CharField(max_length=10, default='license')
    user = models.ForeignKey(AutoUser, on_delete = models.CASCADE, related_name = 'license')
    title = models.CharField(max_length=200)
    score = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_achieved = models.DateTimeField()
    # upload_image = models.ImageField(null=True, blank=True)
    upload_file = models.FileField(upload_to='documents/%Y/%m/%d/')

class Intern(models.Model):
    category = models.CharField(max_length=10, default='intern')    
    user = models.ForeignKey(AutoUser, on_delete= models.CASCADE, related_name = 'intern')
    title = models.CharField(max_length=200)
    summary = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField()
    # upload_image = models.ImageField(null=True, blank=True)
    upload_file = models.FileField(upload_to='documents/%Y/%m/%d/')

class Club(models.Model):
    category = models.CharField(max_length=10, default='club')
    user = models.ForeignKey(AutoUser, on_delete = models.CASCADE, related_name = 'club')
    title = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    summary = models.TextField()
    upload_file = models.FileField(upload_to='documents/%Y/%m/%d/')


class Paper(models.Model):
    category = models.CharField(max_length=10, default='paper')
    user = models.ForeignKey(AutoUser, on_delete= models.CASCADE, related_name = 'paper')
    title = models.CharField(max_length=200)
    summary = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    upload_file = models.FileField(upload_to='documents/%Y/%m/%d/')

class Other(models.Model):
    category = models.CharField(max_length=10, default='other')
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name = 'other')   
    title = models.CharField(max_length=200)
    summary = models.TextField()
    # upload_image = models.ImageField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    upload_file = models.FileField(upload_to='documents/%Y/%m/%d/')