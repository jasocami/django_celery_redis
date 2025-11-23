from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserChangeForm, AdminUserCreationForm
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('last_login', 'is_active', 'is_staff', 'is_superuser', 'date_joined')

    fieldsets = (
        (None, {
            'fields': ('password',)
            }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
            }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser'),
        }),
        ('Django permissions', {
            'classes': ['collapse in'],
            'fields': ('groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ['wide'],
            'fields': ('email',  'password1', 'password2',),
        }),
    )

    form = UserChangeForm
    add_form = AdminUserCreationForm

    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = ('groups', 'user_permissions')
    readonly_fields = ['date_joined']