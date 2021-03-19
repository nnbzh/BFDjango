from django.shortcuts import render

# Create your views here.
from main import tasks


def all(request):
    data = tasks.get_tasks()
    return render(request, 'index.html', {"tasks": data})


def completed(request):
    data = filter(filter_completed, tasks.get_tasks())
    return render(request, 'index.html', {"tasks": data})


def filter_completed(task):
    if task['is_done']:
        return True
    return False
