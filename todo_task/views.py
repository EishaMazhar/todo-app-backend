from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from rest_framework import generics
from rest_framework.decorators import api_view

from .models import TodoTask
from django.shortcuts import render

# Create your views here.
from .serializers import TodoTaskSerializer


# @csrf_exempt
# def get_todo_task(request):
#     if request.method == 'GET':
#         tasks = TodoTask.objects.all()
#         all_tasks = [model_to_dict(x) for x in tasks]
#         # task_dict= model_to_dict(tasks)
#         return JsonResponse(all_tasks, safe=False)
#     else:
#         return HttpResponse('Invalid method called')
#
#
# @csrf_exempt
# def create_todo_task(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         description = request.POST.get('description')
#         is_completed = bool(request.POST.get('is_completed'))
#         task_obj = TodoTask(title=title, description=description, is_completed=is_completed)
#         task_obj.save()
#         return JsonResponse({'status': True, 'msg': 'successful'})


class RetrieveUpdateDestroyTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoTask.objects.all()
    serializer_class = TodoTaskSerializer(many=True)


class CreateTodoList(generics.ListCreateAPIView):
    queryset = TodoTask.objects.all()
    serializer_class = TodoTaskSerializer(many=True)
