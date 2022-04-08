from django.urls import path, include

from .views import TodoViewSet
from rest_framework import routers

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'', TodoViewSet)

urlpatterns = [
    path('', include(router.urls), name="todo-user"),
]
