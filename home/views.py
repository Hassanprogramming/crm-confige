from django.views import View
from django.views.generic import DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from .forms import * 
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from product.models import *
from django.http import JsonResponse
from .models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Count


# Create your views here.
class HomeView(View):
    def get(self, request):
        factors = Factor.objects.all()
        services = service.objects.all()
        checked_services_count = services.filter(checks=True).count()
        unchecked_services_count = services.filter(checks=False).count()
        total_services_count = services.count()
        latest_customers = Customer.objects.all().order_by('-id')[:10]
        latest_users = User.objects.all().order_by('-id')[:5]
        return render(request, 'home/home.html', {'factors': factors, 'services': services,
                                                'latest_customers': latest_customers, 'latest_users': latest_users,
                                                'unchecked_services_count': unchecked_services_count, 'total_services_count': total_services_count,
                                                'checked_services_count': checked_services_count})

#### factores views ####

class FactorView(View):
    @method_decorator(login_required)
    def get(self, request):
        if request.user.is_staff:
            factor = Factor.objects.all()
        else:
            factor = Factor.objects.filter(user=request.user)
        return render(request, 'home/factors.html', {'factor': factor})
    
    
class AddFactorView(View):
    @method_decorator(login_required)
    def get(self, request):
        category = Category.objects.filter(display=True)
        product = Product.objects.all()
        customer =  Customer.objects.all()
        factor = Factor.objects.all()
        form = Add_Factor_Form()
        context = {
            'form': form,
            'factor': factor,
            'category': category,
            'product': product,
            'customer': customer,
        }
        return render(request, 'home/add-factors.html', context)
    
    @method_decorator(login_required)
    def post(self, request):
        form = Add_Factor_Form(request.POST, request.FILES)
        print(form.data)
        if form.is_valid():
            new_factor = form.save(commit=False)  # Create factor instance without saving to the database
            new_factor.user = request.user  # Assign the currently logged-in user to the 'user' field
            new_factor.save()
            print(request.POST)
            print(form.cleaned_data)
            return HttpResponseRedirect(reverse('factor'))
        else:
            context = {
                'form': form
            }
            return render(request, 'home/add-factors.html', context)


class EditFactorView(View):
    @method_decorator(login_required)
    def get(self, request, pid):
        factors = get_object_or_404(Factor, pk=pid)
        form = Edit_Factor_Form(instance=factors)
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
        print(form.data)
        print(form.errors)
        if form.is_valid():
            new_factor = form.save(commit=False)  # Create factor instance without saving to the database
            new_factor.user = request.user  # Assign the currently logged-in user to the 'user' field
            new_factor.save()
            print(request.POST)
            print(form.cleaned_data)
            return redirect('factor')
        else:
            context = {
                'form': form,
                'factors': factors,
            }
        return render(request, 'home/edit_factor.html', context)
        
        
class FactorDeleteView(DeleteView):
    model = Factor
    template_name = 'home/delete_factors_confirmation.html'  # Create a template for confirmation
    success_url = reverse_lazy('factor')  # URL to redirect to after successful deletion
    
    @method_decorator(login_required)
    def get(self, request, pk):
        factor = get_object_or_404(Factor, pk=pk)
        return render(request, self.template_name, {'factor': factor})
    
    @method_decorator(login_required)
    def post(self, request, pk):
        factor = get_object_or_404(Factor, pk=pk)
        factor.delete()
        return redirect(self.success_url)
    

#### services views ####


class ServiceView(View):
    @method_decorator(login_required)
    def get(self, request):
        if request.user.is_admin:
            services = service.objects.all()
        else:
            services = service.objects.filter(user=request.user)
        return render(request, 'home/service.html', {'services': services})


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
        form = Add_Service_Form(request.POST, request.FILES)
        print(form.data)
        if form.is_valid():
            new_factor = form.save(commit=False)  # Create factor instance without saving to the database
            new_factor.user = request.user  # Assign the currently logged-in user to the 'user' field
            new_factor.save()
            print(request.POST)
            print(form.cleaned_data)
            return HttpResponseRedirect(reverse('service'))
        else:
            context = {
                'form': form
            }
            return render(request, 'home/add_service.html', context)


class EditServiceView(View):
    @method_decorator(login_required)    
    def get(self, request, pid):
        servicees = get_object_or_404(service, pk=pid)
        form = Edit_Service_Form(instance=servicees)
        context = {
            'form': form,
            'servicees': servicees,
        }
        return render(request, 'home/edit_service.html', context)
    
    @method_decorator(login_required)
    def post(self, request, pid):
        servicees = get_object_or_404(service, pk=pid)
        form = Edit_Service_Form(request.POST, request.FILES, instance=servicees)
        print(form.data)
        if form.is_valid():
            new_factor = form.save(commit=False)  # Create factor instance without saving to the database
            new_factor.user = request.user  # Assign the currently logged-in user to the 'user' field
            new_factor.save()
            print(request.POST)
            print(form.cleaned_data)
            return redirect('service')
        else:
            context = {
                'form': form,
                'servicees': servicees,
            }
        return render(request, 'home/edit_service.html', context)
        

class ServicDeleteView(DeleteView):
    model = service
    template_name = 'home/delete_services_confirmation.html'  # Create a template for confirmation
    success_url = reverse_lazy('service')  # URL to redirect to after successful deletion
    
    @method_decorator(login_required)
    def get(self, request, pk):
        servic = get_object_or_404(service, pk=pk)
        return render(request, self.template_name, {'servic': servic})
    
    @method_decorator(login_required)
    def post(self, request, pk):
        servic = get_object_or_404(service, pk=pk)
        servic.delete()
        return redirect(self.success_url)        
        
        

class ProductDetailsView(View):
    def get(self, request, *args, **kwargs):
        product_id = self.request.GET.get('product_id')
        try:
            product = get_object_or_404(Product, pk=product_id)
            product_details = {
                'name': product.name,
                'dec': product.dec,
                'price': product.price,
                'image_url': product.imageURL,
                # Add more fields as needed
            }
            return JsonResponse(product_details)
        except Product.DoesNotExist:
            return JsonResponse({'error': 'Product not found'}, status=404)

        return JsonResponse({'error': 'Invalid request'}, status=400)
    

#### Ajax for charts #### 
    
class ChartDataView(View):
    def get(self, request, *args, **kwargs):
        # Calculate the counts
        total_customers = Customer.objects.count()
        called_count = Customer.objects.filter(called=True).count()
        be_called_count = Customer.objects.filter(be_called=True).count()
        
        # Calculate percentages
        called_percentage = (called_count / total_customers) * 100 if total_customers > 0 else 0
        be_called_percentage = (be_called_count / total_customers) * 100 if total_customers > 0 else 0

        data = {
            "labels": ["مشتری تماس گرفته", "ما با مشتری تماس گرفته ایم"],
            "data": [called_count, be_called_count],
            "percentages": [called_percentage, be_called_percentage],
            "backgroundColor": ["#F7604D", "#4ED6B8"],
        }
        return JsonResponse(data)


class BarChartDataView(View):
    def get(self, request, *args, **kwargs):
        # Query the data you need from the Factor model
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        total_factors_count = Factor.objects.count()
        checked_factors_count = Factor.objects.filter(checks=True).count()
        unchecked_factors_count = Factor.objects.filter(checks=False).count()
        
        queryset = Factor.objects.filter(date__range=[start_date, end_date])


        data = {
            "labels": ["فاکتورها"],
            "datasets": [
                {
                    "label": "مجموع فاکتورها",
                    "data": [total_factors_count],
                    "backgroundColor": "#F7604D",
                },
                {
                    "label": "فاکتورهای پرداخت شده",
                    "data": [checked_factors_count],
                    "backgroundColor": "#4ED6B8",
                },
                {
                    "label": "فاکتورهای پرداخت نشده",
                    "data": [unchecked_factors_count],
                    "backgroundColor": "#A8D582",
                },
            ],
        }
        return JsonResponse(data)
    
from django.db.models.functions import TruncDate


@login_required
def get_user_stats(request):
    # Annotate user statistics with date, name, and counts
    user_stats = User.objects.annotate(
        num_factors=Count('factor'),
        num_services=Count('service'),
        date=TruncDate('date_created')
    ).values('date', 'name', 'num_factors', 'num_services')  # Include 'date' and 'name' in values

    # Prepare the response data
    data = {
        'user_stats': list(user_stats)
    }

    return JsonResponse(data)
