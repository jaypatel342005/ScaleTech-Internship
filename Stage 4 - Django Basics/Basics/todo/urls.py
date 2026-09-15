from django.urls import path , include
from . import views




urlpatterns = [
    path("",views.todo, name="todo"),
    path("delete_todo/<int:id>",views.delete_todo, name="delete_todo"),
    path("create_todo/",views.create_todo, name="create_todo"),
    path("update_todo/<int:id>",views.update_todo, name="update_todo"),
    path("status_todo/<int:id>",views.status_todo, name="status_todo"),
]
