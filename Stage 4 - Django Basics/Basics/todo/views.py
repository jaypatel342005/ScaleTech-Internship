from django.shortcuts import render
from .models import * 

# Create your views here.
def todo(request):
    my_todo = list(Todo.objects.all())

    return render(request, "todo/todo.html" , {"todos" : my_todo})

def delete_todo(request,id):
    Todo.objects.get(id=id).delete()
    return redirect("todo/")


