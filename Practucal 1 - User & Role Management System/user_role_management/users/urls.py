
from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.user_get, name = 'user_get'),
    path('create/',views.user_post, name = 'user_post'),
    path('csrf/', views.get_csrf, name='get_csrf'),
    path('delete/<str:username>/',views.user_delete, name = 'user_delete'),
    path('update/<int:id>/' , views.user_put , name = 'user_put'),
    path('login/',views.login, name = 'login'),
    path('logout/',views.logout, name = 'logout'),
    path('signup/',views.signup, name = 'signup'),
    path('update-multiple/',views.update_multiple, name = 'update_multiple'),
    path('bulk-update/', views.update_multiple_diff, name="bulk-update"),
    path('access-check/<str:module>/' ,views.access_check, name="access-check"),
    path('search/' ,views.user_search, name="user_search"),
    
]
