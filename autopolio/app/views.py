from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.
def login(request):
    if request.method == "POST":
        found_user = auth.authenticate(
            username = request.POST['username'],
            password = request.POST['password']
        )
        if found_user is None:
            error = "아이디 또는 비밀번호가 틀렸습니다"
            return render(request, 'registration/login.html', {'error':error})
        auth.login(request, found_user)
        return redirect('main')
    return render(request, 'registration/login.html')

@login_required(login_url='/registration/login')
def main(request):
    pass

@login_required(login_url='/registration/login')
def create(request):
    pass

@login_required(login_url='/registration/login')
def resume(request, user_pk):
    pass

@login_required(login_url='/registration/login')
def detail_license(request, user_pk, license_pk):
    pass

@login_required(login_url='/registration/login')
def detail_intern(request, user_pk, intern_pk):
    pass

@login_required(login_url='/registration/login')
def detail_club(request, user_pk, club_pk):
    pass

@login_required(login_url='/registration/login')
def detail_paper(request, user_pk, paper_pk):
    pass

@login_required(login_url='/registration/login')
def detail_other(request, user_pk, other_pk):
    pass

@login_required(login_url='/registration/login')
def update_license(request, user_pk, license_pk):
    pass

@login_required(login_url='/registration/login')
def update_intern(request, user_pk, intern_pk):
    pass

@login_required(login_url='/registration/login')
def update_club(request, user_pk, club_pk):
    pass

@login_required(login_url='/registration/login')
def update_paper(request, user_pk, paper_pk):
    pass

@login_required(login_url='/registration/login')
def update_other(request, user_pk, other_pk):
    pass

@login_required(login_url='/registration/login')
def delete_license(request, user_pk, license_pk):
    pass

@login_required(login_url='/registration/login')
def delete_intern(request, user_pk, intern_pk):
    pass

@login_required(login_url='/registration/login')
def delete_club(request, user_pk, club_pk):
    pass

@login_required(login_url='/registration/login')
def delete_paper(request, user_pk, paper_pk):
    pass

@login_required(login_url='/registration/login')
def delete_other(request, user_pk, other_pk):
    pass

@login_required(login_url='/registration/login')
def lookup(request):
    pass

@login_required(login_url='/registration/login')
def blurredlist(request, user_pk):
    pass

@login_required(login_url='/registration/login')
def signup(request):
    if request.method == "POST":
        found_user = User.objects.filter(username=request.POST['username'])
        if len(found_user) > 0:
            error = "User name이 이미 존재합니다"
            return render(request, 'registration/signup.html', {'error':error})
        new_user = User.objects.create_user(
            username = request.POST['username'],
            password = request.POST['password']
        )
        auth.login(request, new_user) 
        return redirect('main')
    return render(request, 'registration/signup.html') 

@login_required(login_url='/registration/login')
def logout(request):
    auth.logout(request)
    return redirect('login')

def lookup(request):
    user=Autouser.objects.filter(user=request.user)
    my_occupation=user.occupation
    filtered_users=Autouser.objects.filter(occupation=my_occupation)
    resumes=Resume.objects.filter(user__occupation=my_occupation)
    licenses=License.objects.filter(occupation=my_occupation)
    papers=Papaer.objects.filter(occupation=my_occupation)
    interns=Intern.objects.filter(occupation=my_occupation)
    others=Other.objects.filter(occupation=my_occupation)
    return render(request, 'templates/7_lookup.html',{'resumes':resumes})

