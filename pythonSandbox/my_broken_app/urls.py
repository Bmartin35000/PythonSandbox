from django.urls import path
from .views import (
    TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView,
    CategoryListView, CategoryDetailView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView,
    TagListView, TagDetailView, TagCreateView, TagUpdateView, TagDeleteView
)

urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('task/new/', TaskCreateView.as_view(), name='task-create'),
    path('task/<int:pk>/edit/', TaskUpdateView.as_view(), name='task-update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('category/new/', CategoryCreateView.as_view(), name='category-create'),
    path('category/<int:pk>/edit/', CategoryUpdateView.as_view(), name='category-update'),
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
    path('tags/', TagListView.as_view(), name='tag-list'),
    path('tag/<int:pk>/', TagDetailView.as_view(), name='tag-detail'),
    path('tag/new/', TagCreateView.as_view(), name='tag-create'),
    path('tag/<int:pk>/edit/', TagUpdateView.as_view(), name='tag-update'),
    path('tag/<int:pk>/delete/', TagDeleteView.as_view(), name='tag-delete'),
]
