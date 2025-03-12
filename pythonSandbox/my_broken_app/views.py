from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task, Category, Tag

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'

class TaskCreateView(CreateView):
    model = Task
    template_name = 'task_form.html'
    fields = ['title', 'description', 'completed', 'category', 'tags']

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'task_form.html'
    fields = ['title', 'description', 'completed', 'category', 'tags']

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'
    success_url = '/'

class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'

class CategoryCreateView(CreateView):
    model = Category
    template_name = 'category_form.html'
    fields = ['name', 'description']

class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'category_form.html'
    fields = ['name', 'description']

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category_confirm_delete.html'
    success_url = '/'

class TagListView(ListView):
    model = Tag
    template_name = 'tag_list.html'

class TagDetailView(DetailView):
    model = Tag
    template_name = 'tag_detail.html'

class TagCreateView(CreateView):
    model = Tag
    template_name = 'tag_form.html'
    fields = ['name']

class TagUpdateView(UpdateView):
    model = Tag
    template_name = 'tag_form.html'
    fields = ['name']

class TagDeleteView(DeleteView):
    model = Tag
    template_name = 'tag_confirm_delete.html'
    success_url = '/'
