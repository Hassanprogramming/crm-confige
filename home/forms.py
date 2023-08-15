from django import forms
from .models import *


class Add_Factor_Form(forms.ModelForm):
    class Meta:
        model = Factor
        fields = ['name', 'customer', 'Category', 'dec', 'checks', 'number', 'price', 'total_price', 'img']
        
class FactorForm(forms.ModelForm):
    class Meta:
        model = Factor
        fields = '__all__'
        
class Edit_Factor_Form(forms.ModelForm):
    class Meta:
        model = Factor
        fields = ['name', 'customer', 'Category', 'dec', 'checks', 'number', 'price', 'total_price', 'img']
        
class Add_Service_Form(forms.ModelForm):
    class Meta:
        model = service
        fields = ['name_service', 'customer', 'dec', 'checks', 'number', 'price', 'total_price', 'img']
        
class ServiceForm(forms.ModelForm):
    class Meta:
        model = service
        fields = '__all__'
        
class Edit_Service_Form(forms.ModelForm):
    class Meta:
        model = service
        fields = ['name_service', 'customer', 'dec', 'checks', 'number', 'price', 'total_price', 'img']
