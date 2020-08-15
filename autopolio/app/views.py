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
    return render(request, '1_main.html')


from .forms import *
from .input import category_input
# @login_required(login_url='/registration/login')
def create(request):
    if request.method=='POST':
        newdoc = category_input(request)
        newdoc.save()
        return redirect('create')
    else:
        license_form=LicenseForm()
        intern_form=InternForm()
        club_form=ClubForm()
        paper_form=PaperForm()
        other_form=OtherForm()

    return render(request, '2_create.html', {
        'license_form': license_form,
        'intern_form':intern_form,
        'club_form':club_form,
        'paper_form':paper_form,
        'other_form':other_form
        })    

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

@login_required(login_url='/registration/login')
def mypage(request):
    auth.logout(request)
    return redirect('login')