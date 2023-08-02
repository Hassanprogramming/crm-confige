from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


# Create your views here.

class RegisterView(View):
    def get(self, request):
        form = Register_Form()
        context = {
            'form': form,
        }
        return render(request, 'account/register.html', context)
    
    def post(self, request):
        form = Register_Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Home'))
        else:
            context = {
                'form': form
            }
            return render(request, 'account/register.html', context)
        
        
class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        context = {
            'form': form,
        }
        return render(request, 'account/login.html', context)
    
    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('Home')
        context={
            'form': form, 
        }
        return render(request, 'account/login.html', context)
    
        
class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('login'))
    
class ProfileEditView(View):
    def get(self,request):
        form = ProfileEdit_Form(instance=request.user)
        context = {
            'form': form
        }
        return render(request, 'account/profile.html', context)
    
    def post(self,request):
        form = ProfileEdit_Form(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile_edit')
        else:
            context = {
                'form': form
            }
            return render(request, 'account/profile.html', context)