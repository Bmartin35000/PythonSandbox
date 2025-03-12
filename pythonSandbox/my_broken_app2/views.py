from rest_framework import generics
from .models import Task, Category
from .serializers import TaskSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse, HttpRequest, JsonResponse 
from django.shortcuts import get_object_or_404
import json

class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get(self, req: HttpRequest):
        print("GET")
        tasksRetrieved = Task.objects.filter(user=req.user)
        print("tasksRetrieved")
        print(tasksRetrieved)
        serial = TaskSerializer(tasksRetrieved, many=True)
        print("serial")
        print(serial)
        tasksSerialized = serial.data
        print("tasksSerialized")
        print(tasksSerialized)
        """
        tasksSerialized = []
        for task in tasksRetrieved:
            tasksSerialized.append(TaskSerializer(task).data)
        """
        return HttpResponse(status=200, content=tasksSerialized)
        #return HttpResponse(status=500)

    def post(self, req: HttpRequest):
        print("POST")
        dictionnary = json.loads(req.body)
        serializer = TaskSerializer(data=dictionnary, partial=True)
        if serializer.is_valid():
            serializer.save(user=req.user)
            return HttpResponse(status=201)
        return HttpResponse(status=500)

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=None)  
    
    def patch(self, req: HttpRequest, pk):
        body = req.body
        body: dict = json.loads(body)
        taskRetrieved = get_object_or_404(Task, user=req.user, pk=pk)
        taskRetrieved = TaskSerializer(taskRetrieved, data=body, partial=True)
        if taskRetrieved.is_valid():
            taskRetrieved.save()
            return JsonResponse(status=200, data=taskRetrieved.data)
        else:
            return HttpResponse(status=400)
        
    def delete(self, req: HttpRequest, pk):
        # Start debugging here
        import pdb;pdb.set_trace()
        taskRetrieved = get_object_or_404(Task, pk=pk)
        taskRetrieved.delete()        
        return HttpResponse(status=204)

class CategoryListCreateView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Task.objects.all()  
