from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import (
    DateField, DateTimeField, DurationField, Field, IntegerField, TimeField,
)
# Create your models here.



class AutoUser(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, default=None)
    name = models.TextField()
    email = models.TextField()
    birth = models.DateField()
    high_school = models.CharField(max_length = 30, null = True, blank = True, default = '고등학교를 입력하세요')
    university = models.CharField(max_length = 30, null = True, blank = True, default = '대학교를 입력하세요')
    major = models.TextField(null = True)
    profile = models.ImageField(null=True, blank=True)

    def __str__(self):
	    return self.name

class License(models.Model):
    user = models.ForeignKey(AutoUser, on_delete = models.CASCADE, related_name = 'license')
    title = models.TextField()
    score = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateField(auto_now_add=True)
    date_achieved = models.DateField()
    # upload_image = models.ImageField(null=True, blank=True)
    upload_file = models.FileField(upload_to='documents/%Y/%m/%d/', null = True, blank = True)

    def __str__(self):
	    return self.title

class Intern(models.Model):
    user = models.ForeignKey(AutoUser, on_delete= models.CASCADE, related_name = 'intern')
    title = models.TextField()
    summary = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    start_date = models.DateField()
    end_date = models.DateField()
    # upload_image = models.ImageField(null=True, blank=True)
    upload_file = models.FileField(upload_to='documents/%Y/%m/%d/')
    
    def __str__(self):
	    return self.title
    
class Club(models.Model):
    user = models.ForeignKey(AutoUser, on_delete = models.CASCADE, related_name = 'club')
    title = models.TextField()
    role = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    summary = models.TextField()
    upload_file = models.FileField(upload_to='documents/%Y/%m/%d/')

    def __str__(self):
	    return self.title

class Paper(models.Model):
    user = models.ForeignKey(AutoUser, on_delete= models.CASCADE, related_name = 'paper')
    title = models.TextField()
    summary = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    upload_file = models.FileField(upload_to='documents/%Y/%m/%d/')

    def __str__(self):
	    return self.title

class Other(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name = 'other')   
    title = models.CharField(max_length=200)
    summary = models.TextField()
    # upload_image = models.ImageField(null=True, blank=True)
    date_added = models.DateField(auto_now_add=True)
    upload_file = models.FileField(upload_to='documents/%Y/%m/%d/')
    
    def __str__(self):
	    return self.title