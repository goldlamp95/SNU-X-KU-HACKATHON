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

        # upload_file.widget.attrs.update({'class' : 'file_input'})
        # def __init__(self, *args, **kwargs):
        #     super(LicenseForm, self).__init__(*args, **kwargs)
        #     print("하이", self.fields['upload_file'].widget.attrs)
        #     self.fields['upload_file'].widget.attrs.update({'class' : 'file_input'})
        # fields = ['user','title','score','date_added','date_achieved', 'upload_file']

class InternForm(forms.ModelForm):
    class Meta:
        model = Intern
        fields = '__all__'
        widgets = {
            'start_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'end_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'summary': forms.Textarea(attrs={'rows':4, 'cols':26}),
        }
        # fields = ['title']

class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = '__all__'
        widgets = {
            'start_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'end_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'summary': forms.Textarea(attrs={'rows':4, 'cols':26}),
        }

class PaperForm(forms.ModelForm):
    class Meta:
        model = Paper
        fields = '__all__'
        widgets = {
            'summary': forms.Textarea(attrs={'rows':4, 'cols':26})
        }
        

class OtherForm(forms.ModelForm):
    class Meta:
        model = Other
        fields = '__all__'
        widgets = {
            'summary': forms.Textarea(attrs={'rows':4, 'cols':26})
        }