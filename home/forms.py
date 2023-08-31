from django import forms
from .models import *

class Add_Factor_Form(forms.ModelForm):
    class Meta:
        model = Factor
        fields = ['name', 'dec_2', 'customer', 'Category', 'dec', 'checks', 'number', 'price', 'total_price', 'img']

class Edit_Factor_Form(forms.ModelForm):
    class Meta:
        model = Factor
        fields = ['name', 'dec_2', 'customer', 'Category', 'dec', 'checks', 'number', 'price', 'total_price', 'img']

class Add_Service_Form(forms.ModelForm):
    class Meta:
        model = service
        fields = ['name_service', 'dec_2', 'customer', 'dec', 'checks', 'number', 'price', 'total_price', 'img']

class Edit_Service_Form(forms.ModelForm):
    class Meta:
        model = service
        fields = ['name_service', 'dec_2', 'customer', 'dec', 'checks', 'number', 'price', 'total_price', 'img']
