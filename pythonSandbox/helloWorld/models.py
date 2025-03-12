from django.db import models

# Create your models here.

class Todo(models.Model): # hérite de la classe Model
    titre = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.titre} {self.createdAt} {self.updatedAt}"