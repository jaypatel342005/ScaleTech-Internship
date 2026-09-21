
from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
   path('',views.role_get, name = 'role_get'),
   path('create/',views.role_post, name = 'role_post'),
   path('update/<int:id>/' , views.role_put , name = 'role_put'),
   path('delete/<int:id>/' , views.role_delete , name = 'role_delete')
]
