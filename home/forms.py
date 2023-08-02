from django import forms
from .models import *


class Add_Factor_Form(forms.ModelForm):
    class Meta:
        model = Factor
        fields = ['user', 'name', 'Category', 'date', 'dec', 'checks', 'number', 'price', 'total_price', 'img']
        
class FactorForm(forms.ModelForm):
    class Meta:
        model = Factor
        fields = '__all__'