from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .forms import AccountCreateForm, AccountChangeForm
from .models import User
from django.utils.translation import ugettext_lazy as _


class AccountUserAdmin(UserAdmin):
    form = AccountChangeForm
    add_form = AccountCreateForm
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser',
                                    'groups', 'user_permissions')}),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )


admin.site.register(User, AccountUserAdmin)
admin.site.site_header = 'Quickie Sauce'
admin.site.unregister(Group)
