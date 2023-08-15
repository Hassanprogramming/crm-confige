from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from .forms import * 
from django.http import HttpResponseRedirect
from django.urls import reverse
from product.models import *
from django.http import JsonResponse
from .models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request, 'home/home.html')

#### factores views ####

class FactorView(View):
    @method_decorator(login_required)
    def get(self, request):
        if request.user.is_staff:
            factor = Factor.objects.all()
        else:
            factor = Factor.objects.filter(user=request.user)
        return render(request, 'home/factors.html', {'factor': factor})
    
class EditFactorView(View):
    @method_decorator(login_required)
    def get(self, request, pid):
        factors = get_object_or_404(Factor, pk=pid)
        form = Edit_Factor_Form()
        product_names = Product.objects.all()
        factor_details = Factor.objects.all()
        context = {
            'form': form,
            'factors': factors,
            'product_names': product_names,
            'factor_details': factor_details,
        }
        return render(request, 'home/edit_factor.html', context)
    
    @method_decorator(login_required)
    def post(self, request, pid):
        factors = get_object_or_404(Factor, pk=pid)
        form = Edit_Factor_Form(request.POST, request.FILES, instance=factors)
        if form.is_valid():
            new_factor = form.save(commit=False)  # Create factor instance without saving to the database
            new_factor.user = request.user  # Assign the currently logged-in user to the 'user' field
            new_factor.save()
            return redirect('factor')
        else:
            context = {
                'form': form,
                'factors': factors,
            }
        return render(request, 'home/edit_factor.html', context)

class AddFactorView(View):
    @method_decorator(login_required)
    def get(self, request):
        category = Category.objects.filter(display=True)
        product = Product.objects.all()
        factor = Factor.objects.all()
        form = Add_Factor_Form()
        context = {
            'form': form,
            'factor': factor,
            'category': category,
            'product': product
        }
        return render(request, 'home/add-factors.html', context)
    
    @method_decorator(login_required)
    def post(self, request):
        form = Add_Factor_Form(request.POST)
        form.fields['Category'].widget.attrs['id'] = 'custom-category-id'
        if form.is_valid():
            new_factor = form.save(commit=False)  # Create factor instance without saving to the database
            new_factor.user = request.user  # Assign the currently logged-in user to the 'user' field
            new_factor.save()
            return HttpResponseRedirect(reverse('factor'))
        else:
            context = {
                'form': form
            }
            return render(request, 'home/add-factors.html', context)

#### services views ####

class ServiceView(View):
    @method_decorator(login_required)
    def get(self, request):
        if request.user.is_admin:
            services = service.objects.all()
        else:
            services = service.objects.filter(user=request.user)
        return render(request, 'home/service.html', {'services': services})

class EditServiceView(View):
    @method_decorator(login_required)    
    def get(self, request, pid):
        servicees = get_object_or_404(service, pk=pid)
        form = Edit_Service_Form()
        context = {
            'form': form,
            'servicees': servicees,
        }
        return render(request, 'home/edit_service.html', context)
    
    @method_decorator(login_required)
    def post(self, request, pid):
        servicees = get_object_or_404(service, pk=pid)
        form = Edit_Service_Form(request.POST, request.FILES, instance=servicees)
        if form.is_valid():
            new_factor = form.save(commit=False)  # Create factor instance without saving to the database
            new_factor.user = request.user  # Assign the currently logged-in user to the 'user' field
            new_factor.save()
            return redirect('service')
        else:
            context = {
                'form': form,
                'servicees': servicees,
            }
        return render(request, 'home/edit_service.html', context)


class AddServiceView(View):
    @method_decorator(login_required)
    def get(self, request):
        servic = service.objects.all()
        form = Add_Service_Form()
        context = {
            'form': form,
            'servic': servic
        }
        return render(request, 'home/add_service.html', context)
    
    @method_decorator(login_required)
    def post(self, request):
        form = Add_Service_Form(request.POST)
        if form.is_valid():
            new_factor = form.save(commit=False)  # Create factor instance without saving to the database
            new_factor.user = request.user  # Assign the currently logged-in user to the 'user' field
            new_factor.save()
            return HttpResponseRedirect(reverse('service'))
        else:
            context = {
                'form': form
            }
            return render(request, 'home/add_service.html', context)
        
        
#### loading product base on category ####
class LoadProductsView(View):
    def get(self, request):
        category_id = request.GET.get('category_id')
        products = Product.objects.filter(Category=category_id) if category_id else Product.objects.all()
        
        product_list = []
        for product in products:
            product_list.append({
                'name': product.name,
                'price': product.price,
                # Add more fields as needed
            })
        return JsonResponse({'products': product_list})
    
#### loading product details ####

# class ProductDetailsView(View):
#     def get(self, request):
#         product_id = request.GET.get('product_id')
#         try:
#             product = Product.objects.get(pk=product_id)
#             product_details = {
#                 'price': product.price,
#                 # Add more details as needed
#             }
#             return JsonResponse({'product': product_details})
#         except Product.DoesNotExist:
#             return JsonResponse({'error': 'Product not found.'}, status=404)
