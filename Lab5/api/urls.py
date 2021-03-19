from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register(r'todos', viewset=views.TodoViewSet, basename='todos')
router.register(r'tasks', viewset=views.TaskViewSet, basename='todos')

urlpatterns = [
    path('', include(router.urls))
]
