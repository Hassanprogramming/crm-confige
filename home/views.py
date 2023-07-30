from django.views import View
from django.shortcuts import render
from .forms import * 
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request, 'home/home.html')


class FactorView(View):
    def get(self, request):
        factor = Factor.objects.all()
        return render(request, 'home/factores.html', {'factor': factor})
    
class AddFactorView(View):
    def get(self, request):
        factor = Factor.objects.all()
        form = Add_Factor_Form()
        context = {
            'form': form,
            'factor': factor
        }
        return render(request, 'home/add-factor.html', context)
    
    def post(self, request):
        form = Add_Factor_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('factor'))
        else:
            context = {
                'form': form
            }
            return render(request, 'home/add-factor.html', context)
    
