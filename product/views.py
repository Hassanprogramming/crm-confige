from django.views import View
from django.shortcuts import render

# Create your views here.
class ProductsView(View):
    def get(self, request):
        return render(request, 'products/products.html')

class Add_ProductsView(View):
    def get(self, request):
        return render(request, 'products/add-products.html')

class Edit_ProductsView(View):
    def get(self, request):
        return render(request, 'products/edit-products.html')