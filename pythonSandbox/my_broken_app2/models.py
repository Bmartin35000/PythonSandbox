from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.IntegerField()  

    def __str__(self):
        return self.name

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('H', 'Haute'),  
        ('M', 'Moyenne'),
        ('L', 'Basse'),
    ]
    title = models.CharField(max_length=255)  
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    priority = models.CharField(choices=PRIORITY_CHOICES, max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"name : {self.title} completed : {self.completed}"