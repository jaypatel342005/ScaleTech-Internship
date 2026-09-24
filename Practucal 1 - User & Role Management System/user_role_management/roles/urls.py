
from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
   path('',views.role_get, name = 'role_get'),
   path('create/',views.role_post, name = 'role_post'),
   path('update/<int:id>/' , views.role_put , name = 'role_put'),
   path('delete/<int:id>/' , views.role_delete , name = 'role_delete'),
   path('access/update/' , views.access_update , name = 'access_update'),
   path('access/remove/', views.access_remove, name='access_remove'),
   path('search/',views.role_search, name='role_search')

]
