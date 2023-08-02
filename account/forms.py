from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm



class Register_Form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'phone', 'password', 'email']
        
class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        
class LoginForm(AuthenticationForm):
    pass