from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='Home'),
    path('factor/', FactorView.as_view(), name='factor'),
    path('add_factor/', AddFactorView.as_view(), name='add_factor'),
    path('factor/<int:pid>/', EditFactorView.as_view(), name="edit_factor"),
    path('service/', ServiceView.as_view(), name="service"),
    path('add_service/', AddServiceView.as_view(), name='add_service'),
    path('service/<int:pid>/', EditServiceView.as_view(), name="edit_service"),
    path('load-products/', LoadProductsView.as_view(), name='load_products'),
    # path('product/<int:pk>/', ProductDetailsView.as_view(), name='product-detail'),
]
