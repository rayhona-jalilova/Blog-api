from django.contrib import admin

# Register your models here.
from django.contrib import admin 
from django.contrib.auth.admin import UserAdmin
from .forms import CustomerUserCreationForm, CustomerUserChangeForm 
from .models import CustomerUser
class CustomerUserAdmin(UserAdmin): 
    add_form = CustomerUserCreationForm 
    form = CustomerUserChangeForm 
    model = CustomerUser 
    list_display = [
        "email", 
        "username", 
        "name", 
        "is_staff",
] 
fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("name",)}),) 
add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("name",)}),)

admin.site.register(CustomerUser, CustomerUserAdmin)