from django.urls import path
from .views import *

urlpatterns = [
    path('products/', ProductsView.as_view(), name='products'),
    path('add_products/', Add_ProductsView.as_view(), name='add_products'),
    path('edit_products/', Edit_ProductsView.as_view(), name='edit_products'),
]