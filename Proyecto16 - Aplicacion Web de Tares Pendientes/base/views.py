from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from base.models import Tarea

class ListaPendientes(ListView):
    model = Tarea
    context_object_name = 'tareas'

class DetalleTarea(DetailView):
    model = Tarea
    context_object_name = 'tarea_detalle'
