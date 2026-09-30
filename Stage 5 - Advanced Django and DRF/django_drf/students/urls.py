from django.urls import path
from .views import students_api,student_detail

urlpatterns = [
    path('',students_api, name='students_api'),
    path('<int:id>/',student_detail, name='student_detail'),
]
