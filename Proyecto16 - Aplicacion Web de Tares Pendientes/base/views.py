from django.shortcuts import render
from django.views.generic import ListView
from base.models import Tarea


class ListaPendientes(ListView):
    model = Tarea
    context_object_name = 'tareas'
