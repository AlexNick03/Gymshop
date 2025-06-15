from django.contrib import admin
from accounts.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'is_subscribed','is_staff', 'is_active', 'is_superuser']

admin.site.register(User, UserAdmin)

class PasswordResetAdmin(admin.ModelAdmin):
    list_display = ['user', 'token', 'created_at']
    search_fields = ['user__username', 'token']
    list_filter = ['created_at']