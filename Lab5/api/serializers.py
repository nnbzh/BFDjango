from rest_framework import serializers
from api.models import Task, Todo, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'last_name', 'first_name', 'email', 'last_name', 'is_staff')


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'name')


class TasksSerializer(serializers.ModelSerializer):
    todo_id = serializers.IntegerField(read_only=False)
    owner_id = serializers.IntegerField(read_only=False)

    class Meta:
        model = Task
        fields = ('id', 'task', 'due_date', 'owner', 'created_at', 'is_done')