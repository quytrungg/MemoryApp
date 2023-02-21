from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.

from .models import Memory

class MemoryList(ListView):
    model = Memory
    context_object_name = 'memories'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['memories'] = context['memories'].filter(user=self.request.user)
    #     context['count'] = context['memories'].filter(complete=False).count()

    #     search_input = self.request.GET.get('search-area') or ''
    #     if search_input:
    #         context['memories'] = context['memories'].filter(title__icontains=search_input)
        
    #     context['search_input'] = search_input

    #     return context

class MemoryDetail(DetailView):
    model = Memory
    context_object_name = 'memory'
    template_name = 'base/memory.html'
