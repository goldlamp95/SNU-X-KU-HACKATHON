from .models import *

def category_input(request):
    if request.POST['category'] == 'license':
        # license_form=LicenseForm(request.POST, request.FILES)
        newdoc = License(
            user = request.user,
            title=request.POST['title'],
            score = request.POST['score'],
            date_achieved = request.POST['date_achieved'],
            upload_file=request.FILES['upload_file']
        )
    elif request.POST['category'] == 'intern':
        # intern_form = InternForm(request.POST, request.FILES)
        newdoc = Intern(
            user = request.user,
            title=request.POST['title'],
            summary=request.POST['summary'],
            start_date = request.POST['start_date'],
            end_date = request.POST['end_date'],
            upload_file=request.FILES['upload_file']
        )
    elif request.POST['category'] == 'club':
        # club_form = ClubForm(request.POST, request.FILES)
        newdoc = Club(
            user = request.user,
            title=request.POST['title'],
            role = request.POST['role'],
            summary=request.POST['summary'],
            start_date = request.POST['start_date'],
            end_date = request.POST['end_date'],
            upload_file=request.FILES['upload_file']
        )
    elif request.POST['category'] == 'paper':
        # paper_form = PaperForm(request.POST, request.FILES)
        newdoc = Paper(
            user = request.user,
            title=request.POST['title'],
            summary=request.POST['summary'],
            upload_file=request.FILES['upload_file']    
        )
    elif request.POST['category'] == 'other':
        # other_form=OtherForm(request.POST, request.FILES)
        # if other_form.is_valid():
        # print(request.user)
        newdoc = Other(
            user = request.user,
            title=request.POST['title'],
            summary=request.POST['summary'],
            upload_file=request.FILES['upload_file']
            )
    else:
        print('error')
        return
    return newdoc