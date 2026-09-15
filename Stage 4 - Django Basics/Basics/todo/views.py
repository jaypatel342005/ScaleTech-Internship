from django.shortcuts import render
from .models import * 
from django.shortcuts import redirect

# Create your views here.
def todo(request):
    my_todo = list(Todo.objects.all())

    return render(request, "todo/todo.html" , {"todos" : my_todo})

def delete_todo(request,id):
    Todo.objects.get(id=id).delete()
    return redirect("/todo/")


def create_todo(request):
    if request.method == "POST":
        data = request.POST
        title =  data.get('title')
        desc = data.get('description')
        prio = data.get('priority')
        stat = data.get('status')

        newTodo = Todo.objects.create(
            title = title,
            description = desc,
            priority = prio,
            status = stat,
        )

        return redirect("/todo/")
    else:
        return render(request, "todo/create_todo.html")

def update_todo(request,id):
    if request.method == "POST":
        data = request.POST
        title =  data.get('title')
        desc = data.get('description')
        prio = data.get('priority')
        stat = data.get('status')

        newTodo = Todo.objects.filter(id=id).create(
            title = title,
            description = desc,
            priority = prio,
            status = stat,
        )

        return redirect("/todo/")
    else:
        my_todo = Todo.objects.get(id=id)
        return render(request, "todo/update_todo.html", {"todo": my_todo})

def status_todo(request,id):
    my_todo = Todo.objects.get(id=id)
    if my_todo.status == 'PENDING':
        my_todo.status = 'COMPLETED'
    else:
        my_todo.status = 'PENDING'
    my_todo.save()
    return redirect("/todo/")
        