from django.shortcuts import render, redirect
from .models import * 
from django.contrib.auth.decorators import login_required , permission_required
from django.contrib import messages
from .forms import TodoForm



# Create your views here.
# GET request to get all the todos
@login_required(login_url="/auth/login_user")
@permission_required("todo.view_todo")
def todo(request):

    my_todo = list(Todo.objects.all())

    return render(request, "todo/todo.html" , {"todos" : my_todo})


# delete a todo 
@login_required(login_url="/auth/login_user")
# @permission_required("todo.delete_todo")
def delete_todo(request,id):
    if not request.user.has_perm("todo.delete_todo"):
        messages.error(request, "You don't have permission to delete a todo")
        return redirect("/todo/")
    Todo.objects.get(id=id).delete()
    return redirect("/todo/")

# create a todo
@login_required(login_url="/auth/login_user")
# @permission_required("todo.add_todo")
def create_todo(request):
    if not request.user.has_perm("todo.add_todo"):
        messages.error(request, "You don't have permission to create a todo")
        return redirect("/todo/")
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

# update a todo using manual forms (commented out)
# def update_todo(request,id):
#     if request.method == "POST":
#         data = request.POST
#         title =  data.get('title')
#         desc = data.get('description')
#         prio = data.get('priority')
#         stat = data.get('status')

#         newTodo = Todo.objects.filter(id=id).create(
#             title = title,
#             description = desc,
#             priority = prio,
#             status = stat,
#         )

#         return redirect("/todo/")
#     else:
#         my_todo = Todo.objects.get(id=id)
#         return render(request, "todo/update_todo.html", {"todo": my_todo})

# update a todo using model forms
@login_required(login_url="/auth/login_user")
# @permission_required("todo.change_todo")
def update_todo(request,id):
    if not request.user.has_perm("todo.change_todo"):
        messages.error(request, "You don't have permission to update a todo")
        return redirect("/todo/")
    if request.method == "POST":
        todo_obj = Todo.objects.get(id=id)
        form = TodoForm(request.POST, instance=todo_obj)
        if form.is_valid():
            form.save()
        return redirect("/todo/")
    else:
        my_todo = Todo.objects.get(id=id)
        form = TodoForm(instance=my_todo)
        return render(request, "todo/update_todo.html", {"todo": my_todo , "form": form})


# change the status of a todo
@login_required(login_url="/auth/login_user")

def status_todo(request,id):
    my_todo = Todo.objects.get(id=id)
    if my_todo.status == 'PENDING':
        my_todo.status = 'COMPLETED'
    else:
        my_todo.status = 'PENDING'
    my_todo.save()
    return redirect("/todo/")
        