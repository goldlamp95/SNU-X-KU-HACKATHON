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
    return render (request, 'registration/login.html')

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
    # # for check
    # license_documents = License.objects.all()
    # intern_documents = Intern.objects.all()
    # club_documents = Club.objects.all()
    # paper_documents = Paper.objects.all()
    # other_documents = Other.objects.all()
    return render(request, '2_create.html', {
        # 'license_documents': license_documents,
        # 'intern_documents': intern_documents, 
        # 'club_documents': club_documents, 
        # 'paper_documents': paper_documents, 
        # 'other_documents': other_documents,  
        'license_form': license_form,
        'intern_form':intern_form,
        'club_form':club_form,
        'paper_form':paper_form,
        'other_form':other_form
        })    


def resume(request, user_pk):
    if request.method == 'GET':
        profile = AutoUser.profile
        licenses = License.objects.filter(user__id=user_pk)
        interns = Intern.objects.filter(user__id=user_pk)
        clubs = Club.objects.filter(user__id=user_pk)
        papers = Paper.objects.filter(user__id=user_pk)
        others = Other.objects.filter(user__id=user_pk)

        resumes = {
            'profile' : profile,
            'licenses':licenses,
            'interns': interns,
            'clubs': clubs,
            'papers': papers,
            'others': others
        }
        return render(request, '3_resume.html', resumes)


 
def detail_license(request, user_pk, license_pk):
    license = License.objects.get(pk = license_pk)
    return render(request, '4_detail_license.html', {'license': license})

        


@login_required(login_url='/registration/login')
def detail_intern(request, user_pk, intern_pk):
    intern = Intern.objects.get(pk = intern_pk)
    return render(request, '4_detail_intern.html', {'intern' : intern })

@login_required(login_url='/registration/login')
def detail_club(request, user_pk, club_pk):
    club = Club.objects.get(pk = club_pk)
    return render(request, '4_detail_club.html', {'club' : club })

@login_required(login_url='/registration/login')
def detail_paper(request, user_pk, paper_pk):
    paper = Paper.objects.get(pk = paper_pk)
    return render(request, '4_detail_paper.html', {'paper' : paper })


@login_required(login_url='/registration/login')
def detail_other(request, user_pk, other_pk):
    other = Other.objects.get(pk = other_pk)
    return render(request, '4_detail_paper.html', {'other' : other  })

@login_required(login_url='/registration/login')
def update_license(request, user_pk, license_pk):
    if request.method == 'POST':
        License.objects.filter(pk = license_pk).update(
            title = request.POST['title'],
            score = request.POST['score'],
            # date_added = request.POST['date_added'],
            date_achieved = request.POST['date_achieved'],
            upload_file = request.POST['upload_file']

        )
        return redirect('resume', user_pk)
    return render(request, '5_update_license.html')

@login_required(login_url='/registration/login')
def update_intern(request, user_pk, intern_pk):
    if request.method == 'POST':
        Intern.objects.filter(pk = intern_pk).update(
            title = request.POST['title'],
            summary = request.POST['summary'],
            # date_added = request.POST['date_added'],
            start_date = request.POST['start_date'],
            end_date = request.POST['end_date'],
            upload_file = request.POST['upload_file']

        )
        return redirect('resume', user_pk)
    return render(request, '5_update_intern.html')

@login_required(login_url='/registration/login')
def update_club(request, user_pk, club_pk):
    if request.method == 'POST':
        Club.objects.filter(pk = club_pk).update(
            title = request.POST['title'],
            summary = request.POST['summary'],
            role = request.POST['role'],
            start_date = request.POST['start_date'],
            end_date = request.POST['end_date'],
            upload_file = request.POST['upload_file']

        )
        return redirect('resume', user_pk)
    return render(request, '5_update_club.html')

@login_required(login_url='/registration/login')
def update_paper(request, user_pk, paper_pk):
    if request.method == 'POST':
        Paper.objects.filter(pk = paper_pk).update(
            title = request.POST['title'],
            summary = request.POST['summary'],
            upload_file = request.POST['upload_file']

        )
        return redirect('resume', user_pk)
    return render(request, '5_update_paper.html')


@login_required(login_url='/registration/login')
def update_other(request, user_pk, other_pk):
    if request.method == 'POST':
          Other.objects.filter(pk = other_pk).update(
              title = request.POST['title'],
              summary = request.POST['summary'],
              upload_file = request.POST['upload_file']

          )
          return redirect('resume', user_pk)
    return render(request, '5_update_other.html')

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
def mypage(request, user_pk):
    pass


def signup(request):
    if request.method == "POST":
        found_user = User.objects.filter(username=request.POST['username'])
        if len(found_user) > 0:
            error = "User name이 이미 존재합니다"
            return render(request, 'registration/signup.html', {'error':error})
        user = User.objects.create_user(
            username = request.POST['username'],
            password = request.POST['password'],
            email = request.POST['email'],
        )
        print(request.FILES)
        user.autouser.name = request.POST['name']
        user.autouser.date = request.POST['date']
        user.autouser.profile = request.FILES['profile']
        user.autouser.high_school = request.POST['high_school']
        user.autouser.university = request.POST['university']
        user.autouser.major = request.POST['major']
        user.autouser.occupation = request.POST['occupation']
        user.save()
        

        return redirect('main')
    else:
        autouser_form = AutoUserForm()
        return render(request, 'registration/signup.html', {'autouser_form':autouser_form}) 

@login_required(login_url='/registration/login')
def logout(request):
    auth.logout(request)
    return redirect('login')

def lookup(request):
    my_occupation=user.AutoUser.occupation
    filtered_users=Autouser.objects.filter(occupation=my_occupation)
    return render(request, 'templates/7_lookup.html',{'filtered_users':filtered_users})

def mypage(request):
    pass