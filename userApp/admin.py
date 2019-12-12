from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import User, UserManager
from .forms import UserAdminChangeForm, UserAdminCreationForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.safestring import mark_safe

User = get_user_model()

# Register your models here.
class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('full_name','email', 'admin', 'phone_number', 'bio', 'img')
    list_filter = ('email','admin', 'staff', 'active')
    fieldsets = (
        (None, {'fields': ('full_name', 'email', 'password','phone_number','bio', 'img')}),
        ('Permissions', {'fields': ('admin', 'staff', 'active',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('full_name','email', 'password1', 'password2', 'phone_number','bio', 'img')}
        ),('Permissions', {'fields': ('admin', 'staff', 'active',)}),
    )
    search_fields = ('email', 'full_name',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
