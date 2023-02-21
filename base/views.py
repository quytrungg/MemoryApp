from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.

from .models import Memory

class MemoryList(ListView):
    model = Memory
    context_object_name = 'memories'

class MemoryDetail(DetailView):
    model = Memory
    context_object_name = 'memory'
    template_name = 'base/memory.html'
