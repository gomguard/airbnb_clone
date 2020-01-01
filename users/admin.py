from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


# admin.site.register(models.User, CustomUserAdmin)
@admin.register(models.User)
# class CustomUserAdmin(admin.ModelAdmin):
class CustomUserAdmin(UserAdmin):
    """ Custom User Admin """

    # list_display = ("username", "gender", "language", "currency", "superhost")
    # list_filter = ("language", "superhost", "currency")

    fieldsets = UserAdmin.fieldsets + (
        ("Custom Field", {"fields": ("avatar", "gender", "bio")}),
    )

