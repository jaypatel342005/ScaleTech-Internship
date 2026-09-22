from django.contrib import admin
from .models import Users


@admin.register(Users)
class Useradmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'email',
        'firstName',
        'lastName',
        'role',
        'is_staff',
        'is_superuser',
        'is_active',
    )

    list_filter = (
        'role',
        'is_staff',
        'is_superuser',
        'is_active',
    )

    search_fields = (
        'username',
        'email',
        'firstName',
        'lastName',
    )

    ordering = ('id',)