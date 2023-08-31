from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.hashers import make_password


# Create your views here.
class AccountView(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'account/accounts.html', {'users':users})

class UserAccountView(View):
    def get(self, request, pid):
        users = get_object_or_404(User, pk=pid)
        form = User_detail_Form(instance=users)
        context = {
            'form': form,
            'users': users
        }
        return render(request, 'account/user_profile.html', context)
    
    def post(self, request, pid):
        users = get_object_or_404(User, pk=pid)
        form = User_detail_Form(request.POST, request.FILES, instance=users)
        if form.is_valid():
            form.save()
            return redirect('account')
        else:
            context = {
                'form': form,
                'users':users
            }
        return render(request, 'account/user_profile.html', context)


class RegisterView(View):
    def get(self, request):
        form = Register_Form()
        context = {
            'form': form,
        }
        return render(request, 'account/register.html', context)
    
    def post(self, request):
        form = Register_Form(request.POST, request.FILES)
        print(form.data)
        print(form.errors)
        if form.is_valid():
            print(form.errors)
            user = form.save(commit=False)

# Perform additional processing, e.g., hashing the password
            user.password = make_password(form.cleaned_data['password1'])

            # Save the user to the database
            user.save()
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
            return redirect('Home')
        else:
            context = {
                'form': form
            }
            return render(request, 'account/profile.html', context)
        
        
@method_decorator(login_required, name='dispatch')
class DeleteAccountView(LoginRequiredMixin, View):
    def get(self, request):
        # Delete the user account and log them out
        user = request.user
        user.delete()
        return redirect('Home')
    
    
class CustomerView(View):
    def get(self, request):
        customer = Customer.objects.all()
        return render(request, 'account/customer.html', {'customer':customer})

class Edit_CustomerView(View):
    def get(self, request, pid):
        customer = get_object_or_404(Customer, pk=pid)
        form = EditeCustomer(instance=customer)
        context = {
            'form': form,
            'customer': customer
        }
        return render(request, 'account/edit_customer.html', context)
    
    def post(self, request, pid):
        customer = get_object_or_404(Customer, pk=pid)
        form = EditeCustomer(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer')
        else:
            context = {
                'form': form,
                'customer':customer
            }
        return render(request, 'account/edit_customer.html', context)

class Add_CustomerView(View):
    def get(self, request):
        customer = Customer.objects.all()
        form = AddCustomer()
        context = {
            'form': form,
            'customer': customer,
        }
        return render(request, 'account/add_customer.html', context)

    def post(self, request):
        form = AddCustomer(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print(form)
            return HttpResponseRedirect(reverse('customer'))
        else:
            context = {
                'form': form
            }
            return render(request, 'account/add_customer.html', context)
