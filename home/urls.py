from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='Home'),
    path('factor/', FactorView.as_view(), name='factor'),
    path('add_factor/', AddFactorView.as_view(), name='add_factor')
]
