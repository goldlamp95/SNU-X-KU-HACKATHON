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
        # fields = ['user','title','score','date_added','date_achieved', 'upload_file']

class InternForm(forms.ModelForm):
    class Meta:
        model = Intern
        fields = '__all__'
        # fields = ['title']

class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = '__all__'

class PaperForm(forms.ModelForm):
    class Meta:
        model = Paper
        fields = '__all__'

class OtherForm(forms.ModelForm):
    class Meta:
        model = Other
        fields = '__all__'