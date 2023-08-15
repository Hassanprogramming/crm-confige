from django.contrib import admin
from .models import *

# Register your models here.

class FactorAdmin(admin.ModelAdmin):
    # Customize how the Factor model is displayed in the admin panel
    list_display = ('name', 'Category', 'date', 'customer', 'checks', 'number', 'price', 'total_price')
    list_filter = ('Category', 'checks')
    search_fields = ('name', 'user__name', 'Category__name')
    ordering = ('name',)
    # ...

admin.site.register(Factor, FactorAdmin)

class ServiceAdmin(admin.ModelAdmin):
    # Customize how the Factor model is displayed in the admin panel
    list_display = ('name_service', 'date', 'customer', 'checks', 'total_price')
    search_fields = ('name_service', 'user__name')
    ordering = ('name_service',)
    # ...

admin.site.register(service, ServiceAdmin)
