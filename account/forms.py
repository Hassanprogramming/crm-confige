from django import forms
from .models import *



class Register_Form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'phone', 'password1', 'password2', 'email']
        
class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class ProfileEdit_Form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'phone', 'email']
        
class User_detail_Form(forms.ModelForm):
    class Meta:
        model = User
        fields = ["phone", "email", "name"]
        
class AddCustomer(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["name", "company_name", "date", "img"]
        
class EditeCustomer(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["name", "company_name", "date", "img"]
