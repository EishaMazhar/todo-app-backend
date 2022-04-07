from django.urls import path, include

from .models import TodoTask
from .views import CreateTodoList, RetrieveUpdateDestroyTodo
from .serializers import TodoTaskSerializer
from rest_framework import viewsets, routers


class TodoViewSet(viewsets.ModelViewSet):
    queryset = TodoTask.objects.all()
    serializer_class = TodoTaskSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'', TodoViewSet)

urlpatterns = [
    path('', include(router.urls), name="todo-user"),
]
