from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
# Create your views here.

from .models import Memory

class MemoryList(ListView):
    model = Memory
    context_object_name = 'memories'

class MemoryDetail(DetailView):
    model = Memory
    context_object_name = 'memory'
    template_name = 'base/memory.html'

class MemoryCreate(CreateView):
    model = Memory
    fields = ['place', 'memory_name', 'description', 'complete']
    success_url = reverse_lazy('memories')

class MemoryUpdate(UpdateView):
    model = Memory
    fields = ['place', 'memory_name', 'description', 'complete']
    success_url = reverse_lazy('memories')
