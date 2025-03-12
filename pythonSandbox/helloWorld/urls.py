from . import views
from django.urls import path

urlpatterns = [
    path('myFirstHelloWorld', views.helloWorld),
    path('todo', views.TodoController.as_view()), # as_view() return le get de la classe todocontroller
    path('todo/<int:id>', views.TodoControllerId.as_view()), # path param
    path('todo/create', views.todoForm), # path param
]
