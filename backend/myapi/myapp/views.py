from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import routers
import json
from myapp.models import ToDo
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt 
def get_todo_list(request):
    if request.method == 'GET':
        todo_list = []
        for todo in ToDo.objects.all():
            todo_list.append({'description': todo.description, 'completed': todo.completed})
    return HttpResponse(json.dumps(todo_list),content_type='text/json')

@csrf_exempt 
def add_todo(request):
    if request.method == 'POST':
        request_body = json.loads(request.body)
        todo = ToDo(description=request_body['description'],completed=request_body['completed'])
        try:
            todo.save()
            response = json.dumps([{'Success': 'ToDo added successfully!'}])
        except: 
            response = json.dumps([{'Error': 'ToDo could not be added'}])
    return HttpResponse(response,content_type='text/json')