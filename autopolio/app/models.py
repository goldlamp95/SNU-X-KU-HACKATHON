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
    high_school = models.CharField(max_length = 30, null = True, blank = True)
    university = models.CharField(max_length = 30, null = True, blank = True)
    major = models.CharField(max_length = 30, null = True)
    profile = models.ImageField(max_length = 30, null=True, blank=True)
    occupation = models.CharField(max_length = 30, null = True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):  
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):  
        instance.profile.save()

class License(models.Model):
    resume = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.TextField()
    score = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_achieved = models.DateTimeField()
    upload_image = models.ImageField(null=True, blank=True)
    upload_file = models.FileField(upload_to="%Y/%m/%d")

class Intern(models.Model):
    resume = models.ForeignKey(User, on_delete= models.CASCADE, related_name = 'intern')
    title = models.TextField()
    summary = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField()
    upload_image = models.ImageField(null=True, blank=True)
    upload_file = models.FileField(upload_to='uploads/%Y/%m/%d/')

class Paper(models.Model):
    resume = models.ForeignKey(Resume, on_delete= models.CASCADE, related_name = 'paper')
    title = models.TextField()
    summary = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    upload_file = models.FileField(upload_to='uploads/%Y/%m/%d/')

class Other(models.Model):
    resume=models.ForeignKey(Resume, on_delete= models.CASCADE, related_name = 'other')
    title = models.TextField()
    summary = models.TextField()
    upload_image = models.ImageField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    upload_file = models.FileField(upload_to='uploads/%Y/%m/%d/')

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)