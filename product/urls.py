from django.urls import path
from .views import *

urlpatterns = [
    path('products/', ProductsView.as_view(), name='products'),
    path('products/<int:pid>/', Edit_ProductsView.as_view(), name='edit_products'),
    path('add_products/', Add_ProductsView.as_view(), name='add_products'),
    path('add_category/', Add_CategoryView.as_view(), name='add_category'),
    path('products/delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('category/delete/<int:pid>/', CategorytDeleteView.as_view(), name='delete_category'),
]
