from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'dni', 'address', 'email', 'username', 'password', 'avatar', 'is_staff',
              'is_active', 'is_superuser']
