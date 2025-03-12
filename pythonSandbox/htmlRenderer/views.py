from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.

def home(req: HttpRequest):
    monContext = {"persons":["Toto","Riri","Fifi","Loulou"]}
    return render(req, "home.html", monContext)

def parent(req: HttpRequest):
    monContext = {}
    return render(req, "parent.html", monContext)

def children(req: HttpRequest):
    monContext = {}
    return render(req, "children.html", monContext)