from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

from .models import Memory

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('memories')

class MemoryList(LoginRequiredMixin, ListView):
    model = Memory
    context_object_name = 'memories'

class MemoryDetail(LoginRequiredMixin, DetailView):
    model = Memory
    context_object_name = 'memory'
    template_name = 'base/memory.html'

class MemoryCreate(LoginRequiredMixin, CreateView):
    model = Memory
    fields = ['place', 'memory_name', 'description', 'complete']
    success_url = reverse_lazy('memories')

class MemoryUpdate(LoginRequiredMixin, UpdateView):
    model = Memory
    fields = ['place', 'memory_name', 'description', 'complete']
    success_url = reverse_lazy('memories')

class MemoryDelete(LoginRequiredMixin, DeleteView):
    model = Memory
    context_object_name = 'memory'
    success_url = reverse_lazy('memories')
