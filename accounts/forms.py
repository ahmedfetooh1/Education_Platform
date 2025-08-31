from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import InstructorProfile


class SignUpForm(UserCreationForm):
    ROLE_CHOICES = (
        ('students','Students'),
        ('instructor','Instructor')
    )
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'E-mail'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))
    role = forms.ChoiceField(choices=ROLE_CHOICES,required=True)
    

    class Meta :
        model = User
        fields = ['username','email','password1','password2']


        
class InstructorProfileForm(forms.ModelForm):
    class Meta :
        model = InstructorProfile
        fields = ['bio','photo','contact_email','header']

