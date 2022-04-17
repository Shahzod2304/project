from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomerUserCreationForm, CustomerUserChangeForm
from .models import CustomerUser

# Register your models here.

class CustomerUserAdmin(UserAdmin):
    add_form = CustomerUserCreationForm
    form = CustomerUserChangeForm
    model = CustomerUser
    
    list_display = ['email','username','first_name','last_name','manzil','is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None,{'fields':('manzil',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None,{'fields':('manzil',)}),
    )

admin.site.register(CustomerUser,CustomerUserAdmin)

