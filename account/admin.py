from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    list_display = ('name', 'phone', 'email', 'is_admin', 'is_second_admin', 'is_third_admin')
    list_filter = ('is_admin', 'is_second_admin', 'is_third_admin')
    search_fields = ('name', 'phone', 'email')
    ordering = ('name',)
    fieldsets = (
        (None, {'fields': ('name', 'phone', 'email', 'password', 'user_permissions', 'groups')}),
        ('Admin Privileges', {'fields': ('is_admin', 'is_second_admin', 'is_third_admin')}),
        ('Important Dates', {'fields': ('date_created',)}),
    )
    readonly_fields = ('date_created',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'phone', 'email', 'password1', 'password2', 'is_admin', 'is_second_admin', 'is_third_admin', 'user_permissions', 'groups'),
        }),
    )

admin.site.register(User, UserAdmin)
