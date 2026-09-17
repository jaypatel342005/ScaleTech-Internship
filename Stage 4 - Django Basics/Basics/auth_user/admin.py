from django.contrib import admin
from .models import Custom_User

# Register your models here.
@admin.register(Custom_User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_admin', 'is_user', 'is_staff', 'is_superuser', 'is_active')
    list_filter = ('is_admin', 'is_user', 'is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('id',)
    
    

