from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
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
        return render(request, 'home/factors.html', {'factor': factor})
    
class EditFactorView(View):
    def get(self, request, pid):
        factor = get_object_or_404(factor, pk=pid)
        form = Add_Factor_Form()
        context = {
            'form': form,
            'factor': factor,
        }
        return render(request, 'home/edit-factors.html', context)
    
    def post(self, request, pid):
        factor = get_object_or_404(Factor, pk=pid)
        form = Add_Factor_Form(request.POST, instance=factor)
        if form.is_valid():
            form.save()
            return redirect('factor')
        else:
            context = {
                'form': form,
                'factor': factor,
            }
        return render(request, 'home/edit-factors.html', context)

class AddFactorView(View):
    def get(self, request):
        factor = Factor.objects.all()
        form = Add_Factor_Form()
        context = {
            'form': form,
            'factor': factor
        }
        return render(request, 'home/add-factors.html', context)
    
    def post(self, request):
        form = Add_Factor_Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('factor'))
        else:
            context = {
                'form': form
            }
            return render(request, 'home/add-factors.html', context)
    
