from django.db import models


class Todos(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)


class Tasks(models.Model):
    task = models.CharField(max_length=255, null=True, blank=True)
    created_date = models.DateField()
    due_on = models.DateField()
    owner = models.CharField(max_length=255, null=True, blank=True)
    mark = models.BooleanField()
    todos = models.ForeignKey(Todos, on_delete=models.CASCADE, related_name='todos')
