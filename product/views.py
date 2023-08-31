from django.views import View
from django.views.generic import DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
class ProductsView(View):
    def get(self, request):
        product = Product.objects.all()
        category = Category.objects.filter(display=True)
        return render(request, 'products/products.html', {'product':product, "category":category})

class Edit_ProductsView(View):
    def get(self, request, pid):
        product = get_object_or_404(Product, pk=pid)
        form = Add_Product_Form()
        context = {
            'form': form,
            'product': product,
        }
        return render(request, 'products/edit-products.html', context)
    
    def post(self, request, pid):
        product = get_object_or_404(Product, pk=pid)
        form = Add_Product_Form(request.POST, request.FILES, instance=product)
        print(form.data)
        if form.is_valid():
            form.save()
            print(request.POST)
            print(form.cleaned_data)
            return redirect('products')
        else:
            context = {
                'form': form,
                'product': product,
            }
        return render(request, 'products/edit-products.html', context)

class Add_ProductsView(View):
    def get(self, request):
        category = Category.objects.filter(display=True)
        form = Add_Product_Form()
        context = {
            'form': form,
            'category': category,
        }
        return render(request, 'products/add-products.html', context)

    def post(self, request):
        form = Add_Product_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('products'))
        else:
            context = {
                'form': form
            }
            return render(request, 'products/add-products.html', context)
    
class Add_CategoryView(View):
    def get(self, request):
        form = Add_Category_Form()
        context = {
            'form': form
        }
        return render(request, 'products/add-category.html', context)

    def post(self, request):
        form = Add_Category_Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('products'))
        else:
            context = {
                'form': form
            }
            print(form)
            return render(request, 'products/add-category.html', context)
        
        
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/delete_product_confirmation.html'  # Create a template for confirmation
    success_url = reverse_lazy('products')  # URL to redirect to after successful deletion
    
    @method_decorator(login_required)
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        return render(request, self.template_name, {'product': product})
    
    @method_decorator(login_required)
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return redirect(self.success_url)        
        
        
class CategorytDeleteView(DeleteView):
    model = Category
    template_name = 'products/category_delete_confirmation.html'  # Create a template for confirmation
    success_url = reverse_lazy('products')  # URL to redirect to after successful deletion
    
    @method_decorator(login_required)
    def get(self, request, pid):
        category = get_object_or_404(Category, pk=pid)
        return render(request, self.template_name, {'category': category})
    
    @method_decorator(login_required)
    def post(self, request, pid):
        category = get_object_or_404(Category, pk=pid)
        category.delete()
        return redirect(self.success_url)        
        
