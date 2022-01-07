
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from django.http import response
from api.models import Task
from api.serializers import TaskSerializers


class Home(APIView):
    def get(self,request):
        helpertext = {
            'Homepage' : '/',
            'list all task' : 'viewlist',
            'add new task' : '/add',
            'detail of task' : '/detail/<str:key>',
            'update task' : '/update/<str:key>',
            'delete task' : '/delete/<str:key>'
        }
        return Response(helpertext)
    

class TaskList(APIView):
    def get(self,request):
        tasks = Task.objects.all()
        serialized_tasks = TaskSerializers(tasks , many = True)
        print(serialized_tasks.data)
        return Response(serialized_tasks.data)
    
class NewTask(APIView):
    def post(self,request):
        new_task = TaskSerializers(data = request.data)
        if new_task.is_valid():
            new_task.save()
        return Response("Task added successfully")
    
class DetailView(APIView):
    def get(self,request,key):
        task = Task.objects.get(id=key)
        serialized_task = TaskSerializers(task , many = False)
        return Response(serialized_task.data)
    
class DeleteTask(APIView):
    def get(self,request,key):
        task = Task.objects.get(id=key)
        task.delete()
        return Response("Task Deleted Successfully")


class UpdateTask(APIView):
    def post(self,request,key):
        task = Task.objects.get(id=key)
        new_task = TaskSerializers(instance=task , data=request.data)
        if new_task.is_valid():
            new_task.save()
        return Response("Updated")