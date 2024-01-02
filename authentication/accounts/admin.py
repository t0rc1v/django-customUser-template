from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = CustomUser

    fieldsets = (
        (None, {"fields": ("email", "phone", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "phone", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    # fieldsets = UserAdmin.fieldsets + (('additional info',{'fields': ['phone']}),)
    # add_fieldsets = UserAdmin.fieldsets + (('additional info',{'fields': ['phone']}),)
    list_display = ["email"]
    search_fields = ["email"]
    list_filter = ["email"]
    ordering = ["email"]
