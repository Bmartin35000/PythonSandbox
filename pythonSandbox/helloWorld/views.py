from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpRequest, HttpResponseRedirect
from django.views import View 
from django.views.decorators.csrf import csrf_exempt 
import json 
from .models import Todo
from .serializers import TodoSerializer
from .forms import TodoForm

def helloWorld(request):
    return HttpResponse("Hello world !")

def todoForm(req: HttpRequest):
    match req.method:
        case "GET":
            return render(req, "todoForm.html", {"form" : TodoForm})
        case "POST":
            form = TodoForm(req.POST)
            if form.is_valid():
                print("ajout de mon super todo !", form.cleaned_data.get("titre"))
                return HttpResponseRedirect("/htmlRenderer/home")

class TodoController(View):
    def get(self, req): # self equivalent de this en java
        todoRetrieved = Todo.objects.all()
        print(todoRetrieved)
        print(TodoSerializer(todoRetrieved, many=True).data)
        return JsonResponse(TodoSerializer(todoRetrieved, many=True).data, safe=False) # TodoSerializer(todoRetrieved, many=True) est un constructeur

    @csrf_exempt # décorateur
    def post(self, req: HttpRequest):
        todoModel = get_object_or_404(Todo, pk=id)

        todoDict = json.loads(req.body) # transforme byte en json dict
        serial = TodoSerializer(data=todoDict)
        if serial.is_valid():
            serial.save() # requete sql create
            todoModel = serial.data
            return JsonResponse(todoModel, safe=False, status=201) 
        return JsonResponse(serial.errors, status=400) # return err du serializer (err sql si besoin)
    
    @csrf_exempt
    def put(self, req: HttpRequest):
        todoDict = json.loads(req.body) # transforme byte en json dict
        todoDto = get_object_or_404(Todo, pk=todoDict["id"])
        serial = TodoSerializer(todoDto, data=todoDict, partial=True) # update l'objet existant sur les champs fournis uniquement
        if serial.is_valid():
            serial.save() # requete sql update
            todoModel = serial.data
            return JsonResponse(todoModel, safe=False, status=201) 
        return JsonResponse("dto incorrect", status=400)

class TodoControllerId(View):
    @csrf_exempt
    def get(self, req: HttpRequest, id):
        todoModel = Todo.objects.get(pk=id)
        todoModel = TodoSerializer(todoModel, many=False).data
        return JsonResponse(todoModel, safe=False, status=200)

    @csrf_exempt
    def delete(self, req: HttpRequest, id):
        """
        try: # try catch
            todoModel = Todo.objects.get(pk=id)
        except Todo.DoesNotExist:
            return JsonResponse("Todo not recognized", safe=False, status=404)
        """
        todoModel = get_object_or_404(Todo, pk=id)
        todoRes = todoModel.delete()
        return JsonResponse("todo deleted", safe=False, status=200)
    
