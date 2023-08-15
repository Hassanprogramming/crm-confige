from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('account/', AccountView.as_view(), name='account'),
    path('account/<int:pid>/', UserAccountView.as_view(), name='user_profile'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile_edit/', ProfileEditView.as_view(), name='profile_edit'),
    path('customer/', CustomerView.as_view(), name='customer'),
    path('customer/<int:pid>/', Edit_CustomerView.as_view(), name='edit_customer'),
    path('add_customer/', Add_CustomerView.as_view(), name='add_customer'),
    #### password reset configrations ####
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    #### change password configrations ####
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('delete_account/', views.DeleteAccountView.as_view(), name='delete_account'),
]
