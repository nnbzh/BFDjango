from django.shortcuts import render
from main.models import Todos, Tasks


# Create your views here.

def get_tasks(request, todo_id):
    tasks = Tasks.objects.filter(todos=id)
    todos = Todos.objects.get(id=id)
    context = {'tasks': tasks, 'todo': todos}

    return render(request, 'tasks.html', context)
#
#
def get_completed_tasks(request, todo_id):
    tasks = Tasks.objects.filter(todos=id, mark=True)
    todos = Todos.objects.get(id=id)
    context = {'tasks': tasks, 'todo': todos}

    return render(request, 'tasks.html', context)


def get_todos(request):
    todos = Todos.objects.all()
    context = {'todos': todos}
    return render(request, 'index.html', context)
