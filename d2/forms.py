from django import forms
from .models import Feedback
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'feedback']
        labels = {
            'name': 'Name',
            'email': 'Email',
            'feedback': 'Feedback',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'feedback': forms.Textarea(attrs={'class': 'form-control'}),
        }

class SignupForm(UserCreationForm):
    password1=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label="Confirm Password (again)",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
       
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':"Email",'last_name':'Last Name','first_name':"First Name"}   
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),'first_name':forms.TextInput(attrs={'class':'form-control'}),'last_name':forms.TextInput(attrs={'class':'form-control'}),'email':forms.TextInput(attrs={'class':'form-control'})}