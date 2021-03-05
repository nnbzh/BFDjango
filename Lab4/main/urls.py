from django.urls import path

from . import views

urlpatterns = [
    path('todos', views.get_todos, name='todos'),
    path('todos/<int:todo_id>/tasks', views.get_tasks, name='todo_tasks'),
    path('todos/<int:todo_id>/tasks/completed', views.get_completed_tasks, name='completed_tasks'),
]