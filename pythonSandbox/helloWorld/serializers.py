from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta: # required for ModelSerializer
        model = Todo
        fields = "__all__"
    