from django.urls import path
from .views import EmployeeView , EmployeeDetail

urlpatterns = [
    path('',EmployeeView.as_view(), name='employees'),
    path('<int:id>/',EmployeeDetail.as_view(), name='employee_detail'),
]
