
from django.urls import path
from .views import TaskListCreateView, TaskDetailView, CategoryListCreateView


urlpatterns = [
    path('tasks/', TaskListCreateView.as_view()),
    path('tasks/<str:pk>/', TaskDetailView.as_view(), name='task-detail'),  
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
]
