from django import forms
from .models import License, Intern, Club, Paper, Other, AutoUser

class AutoUserForm(forms.ModelForm):
    class Meta:
        model = AutoUser
        fields = ['profile']

class LicenseForm(forms.ModelForm):
    class Meta:
        model = License
        fields = '__all__'
        widgets = {
            'date_achieved': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'})
        }
        # fields = ['user','title','score','date_added','date_achieved', 'upload_file']

class InternForm(forms.ModelForm):
    class Meta:
        model = Intern
        fields = '__all__'
        widgets = {
            'start_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'end_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'})
        }
        # fields = ['title']

class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = '__all__'
        widgets = {
            'start_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'end_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'})
        }

class PaperForm(forms.ModelForm):
    class Meta:
        model = Paper
        fields = '__all__'
        

class OtherForm(forms.ModelForm):
    class Meta:
        model = Other
        fields = '__all__'
        