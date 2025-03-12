from django.views.generic import *
from django import forms

class TodoForm(forms.Form):
    titre = forms.CharField()