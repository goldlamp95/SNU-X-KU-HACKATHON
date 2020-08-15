from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import (
    DateField, DateTimeField, DurationField, Field, IntegerField, TimeField,
)
from django.db.models.signals import post_save 
from django.dispatch import receiver  
# Create your models here.



class AutoUser(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.TextField(null=True)
    birth = models.DateField(null=True)
    high_school = models.CharField(max_length = 30, null = True, blank = True, default = '고등학교를 입력하세요')
    university = models.CharField(max_length = 30, null = True, blank = True, default = '대학교를 입력하세요')
    class_year = models.IntegerField(null=True)
    major = models.TextField(null = True)
    profile = models.ImageField(null=True, blank=True)
    occupation=models.TextField(null = True)
    like_users = models.ManyToManyField('self',blank=True,through='Like',symmetrical=False)
    follows = models.ManyToManyField('self',through = 'Follow', blank=True, related_name='followed',symmetrical=False)

    def __str__(self):
        return self.name
    
    @receiver(post_save, sender=User)
    def create_user_AutoUser(sender, instance, created, **kwargs):  
        if created:
            AutoUser.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_AutoUser(sender, instance, **kwargs):  
        instance.autouser.save()


class License(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'license')
    title = models.CharField(max_length=200)
    score = models.IntegerField(default=0, blank=True)
    date_added = models.DateField(auto_now_add=True)
    date_achieved = models.DateField()
    # upload_image = models.ImageField(null=True, blank=True)
    upload_file = models.FileField(upload_to='documents/%Y/%m/%d/')
    category = models.CharField(max_length=10, default='license', blank=True, null=False)

    def __str__(self):
        return self.title

class Intern(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name = 'intern')
    title = models.CharField(max_length=200)
    summary = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    start_date = models.DateField()
    end_date = models.DateField()
    # upload_image = models.ImageField(null=True, blank=True)
    upload_file = models.FileField(upload_to='documents/%Y/%m/%d/',null=True)
    category = models.CharField(max_length=10, default='intern', blank=True, null=False)    
    
    def __str__(self):
        return self.title

class Club(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'club')
    title = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    date_added = models.DateField(auto_now_add=True)
    start_date = models.DateField()
    end_date = models.DateField()
    summary = models.TextField()
    upload_file = models.FileField(upload_to='documents/%Y/%m/%d/', null=True)
    category = models.CharField(max_length=10, default='club', blank=True, null=False)

    def __str__(self):
        return self.title


class Paper(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name = 'paper')
    title = models.CharField(max_length=200)
    summary = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    upload_file = models.FileField(upload_to='documents/%Y/%m/%d/')
    category = models.CharField(max_length=10, default='paper', blank=True, null=False)


    def __str__(self):
        return self.title

class Other(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name = 'other')   
    title = models.CharField(max_length=200)
    summary = models.TextField()
    # upload_image = models.ImageField(null=True, blank=True)
    date_added = models.DateField(auto_now_add=True)
    upload_file = models.FileField(upload_to='documents/%Y/%m/%d/',null=True)
    category = models.CharField(max_length=10, default='other', blank=True, null=False)
    def __str__(self):
        return self.title

class Like(models.Model):
    user = models.ForeignKey(AutoUser,related_name = 'liked_from', on_delete=models.CASCADE)
    liked_user = models.ForeignKey(AutoUser, related_name = 'like_to', on_delete=models.CASCADE)

class Follow(models.Model):
    follow_to = models.ForeignKey(AutoUser, related_name = 'follow_from', on_delete=models.CASCADE)
    follow_from = models.ForeignKey(AutoUser, related_name = 'follow_to', on_delete=models.CASCADE)

    def __str__(self):
        return '{} follows {}'.format(self.follow_from, self.follow_to)