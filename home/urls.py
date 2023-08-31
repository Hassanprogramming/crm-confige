from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='Home'),
    ####Factor urls####
    path('factor/', FactorView.as_view(), name='factor'),
    path('add_factor/', AddFactorView.as_view(), name='add_factor'),
    path('factor/<int:pid>/', EditFactorView.as_view(), name="edit_factor"),
    path('factor/delete/<int:pk>/', FactorDeleteView.as_view(), name='delete_factor'),
    ####Service urls####
    path('service/', ServiceView.as_view(), name="service"),
    path('add_service/', AddServiceView.as_view(), name='add_service'),
    path('service/delete/<int:pk>/', ServicDeleteView.as_view(), name='delete_servic'),
    path('service/<int:pid>/', EditServiceView.as_view(), name="edit_service"),
    path('product_details/', ProductDetailsView.as_view(), name='product_details'),
    path('chart_data/', ChartDataView.as_view(), name='chart_data'),
    path('bar_chart_data/', BarChartDataView.as_view(), name='bar_chart_data'),
    path('get_user_stats/', get_user_stats, name='get_user_stats'),
]
