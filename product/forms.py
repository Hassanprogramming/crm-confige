from django import forms
from .models import *


class Add_Product_Form(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'dec', 'Category', 'img', 'price']
        
class Add_Category_Form(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'checks']
        
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'