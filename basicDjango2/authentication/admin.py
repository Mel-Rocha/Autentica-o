from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email']
    search_fields = ['nome', 'email']
    list_filter = ['is_staff', 'is_active']

admin.site.register(CustomUser, CustomUserAdmin)