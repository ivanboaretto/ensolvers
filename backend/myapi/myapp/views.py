from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import routers
from django.views.decorators.csrf import csrf_exempt
from myapp.serializers import ToDoSerializer
from myapp.models import ToDo

@csrf_exempt 
def get_todo_list(request):
    if request.method == 'GET':
        todo_list = ToDo.objects.all()
        serializer = ToDoSerializer(todo_list,many=True)
        return JsonResponse(serializer.data,safe=False)
    return HttpResponse(status=404)

@csrf_exempt 
def add_todo(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ToDoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    return HttpResponse(status=404)
    
@csrf_exempt
def update_todo(request,pk):
    try: 
        todo = ToDo.objects.get(pk=pk)
    except ToDo.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ToDoSerializer(todo, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        todo.delete()
        return HttpResponse(status=204)