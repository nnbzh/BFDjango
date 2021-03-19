from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

# Create your models here.

class User(AbstractUser):
    username = None
    email = models.EmailField(('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Todo(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)


class Task(models.Model):
    task            = models.CharField(max_length=255, null=True, blank=True)
    created_date    = models.DateField()
    due_date        = models.DateField()
    owner           = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    is_done         = models.BooleanField()
    todo            = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='todo')