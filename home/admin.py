from django.contrib import admin
from .models import *

# Register your models here.

class FactorAdmin(admin.ModelAdmin):
    # Customize how the Factor model is displayed in the admin panel
    list_display = ('name', 'user', 'Category', 'date', 'dec', 'checks', 'number', 'price', 'total_price')
    list_filter = ('user', 'Category', 'checks')
    search_fields = ('name', 'user__name', 'Category__name')
    ordering = ('name',)
    # ...

admin.site.register(Factor, FactorAdmin)