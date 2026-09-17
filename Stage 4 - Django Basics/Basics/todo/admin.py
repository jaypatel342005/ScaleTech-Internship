from django.contrib import admin
from .models import Todo

# Register your models here.
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('status', 'priority', 'created_at')
    search_fields = ('title', 'description')
    ordering = ('id',)
