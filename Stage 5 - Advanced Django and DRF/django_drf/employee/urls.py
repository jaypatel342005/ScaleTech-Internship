from django.urls import path , include
# from .views import EmployeeView , EmployeeDetail 
from .views import  Employees , EmployeeDetail
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewset , EmployeeModelViewSet


router = DefaultRouter()
router.register('employees-viewset', EmployeeViewset, basename='employee-viewset')
router.register('employees-model', EmployeeModelViewSet, basename='employee-model')


urlpatterns = [
    # normal class based view for employees
    # path('',EmployeeView.as_view(), name='employees'),
    # path('<int:id>/',EmployeeDetail.as_view(), name='employee_detail'),
    
    # #mixins and generic viewset
    # path('',Employees.as_view(), name='employees'),
    # path('<int:pk>/',EmployeeDetail.as_view(), name='employee_detail'),

    #generics ListCreateAPIView and RetrieveUpdateDestroyAPIView
    path('',Employees.as_view(), name='employees'),
    path('<int:pk>/',EmployeeDetail.as_view(), name='employee_detail'),

    path('', include(router.urls)),

    #viewset and modelviewset
    # path('',include(router.urls)),
]
