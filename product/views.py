from django.views import View
from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
class ProductsView(View):
    def get(self, request):
        product = Product.objects.all()
        category = Category.objects.filter(display=True)
        return render(request, 'products/products.html', {'product':product, "category":category})

class Edit_ProductsView(View):
    def get(self, request, pid):
        product = get_object_or_404(Product,pk=pid)
        return render(request, 'products/edit-products.html', {'product':product})

class Add_ProductsView(View):
    def get(self, request):
        return render(request, 'products/add-products.html')
    
class Add_CategoryView(View):
    def get(self, request):
        return render(request, 'products/add-category.html')