import json

from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import action

from api.models import Todo, Task
from api.serializers import TodoSerializer, TaskSerializer


# Create your views here.
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    @action(detail=True, methods=['GET'], url_path='completed')
    def completed(self, request, pk):
        data = Task.objects.filter(todo_id=pk, is_done=True)
        serializer = TaskSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
