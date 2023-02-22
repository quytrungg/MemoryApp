from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from social_core.backends.facebook import FacebookOAuth2
# Create your views here.

from .models import Memory

import requests

# graph_url = 'https://graph.facebook.com/v13.0/me'
# fields = 'id,name,email,picture'
# access_token = 'AQCZMY4UA6zbNoHwhmNCCklyS1S0wp-9EBwzlnnZ_fjGHbJkt4giGVXG7dy09q4M35AEBoRFxA03t5sdNdZbLjge7q78IjsW4Uwi2ErEl9nJnCHNB3JL3y25VwBtLBrfLU1VWFHxDHevsJqGsd6z4UZqQhN93rPa27ecZ3Iq88Auw5AQHon1iWFJ386tShB1Dh5HgkNq12yy-Y1KqVGeseFLgCdAla3pdo4hClw3VsIzfr3tjWPjlms1lnWzMoqc5aJyR1ddLGF0ZM4bpFILxJy67tZfx3AiX7QkaY-pzaWT9vnJUQI4ZsgUhhmL9eGYvXpLtddDjgKI5I57RuR027AVGzE0WcCFUMQLhi1rz-CsMmdMXVTvHHinerZTb3c3Yf7iWBo9rWilpH3i-2QB5Lmq&state=UD69Cq3C6Xv0BFM6Y3m6vq5FStlomkOp'

# params = {'fields': fields, 'access_token': access_token}
# response = requests.get(graph_url, params=params)
# data = response.json()
# print(data)

# def my_callback(request):
#     # Retrieve the access token for the authenticated user
#     backend = FacebookOAuth2(request)
#     token = backend.get_access_token(request.GET.get('code'))
#     print(token)

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        backend = FacebookOAuth2(self.request)
        token = backend.get_access_token(self.request.GET.get('code'))
        print('abc', token)
        return reverse_lazy('memories')

class MemoryList(LoginRequiredMixin, ListView):
    model = Memory
    context_object_name = 'memories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['memories'] = context['memories'].filter(user=self.request.user)
        # context['count'] = context['memories'].filter(complete=False).count()

        return context

class MemoryDetail(LoginRequiredMixin, DetailView):
    model = Memory
    context_object_name = 'memory'
    template_name = 'base/memory.html'

class MemoryCreate(LoginRequiredMixin, CreateView):
    model = Memory
    fields = ['place', 'memory_name', 'description', 'complete']
    success_url = reverse_lazy('memories')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(MemoryCreate, self).form_valid(form)

class MemoryUpdate(LoginRequiredMixin, UpdateView):
    model = Memory
    fields = ['place', 'memory_name', 'description', 'complete']
    success_url = reverse_lazy('memories')

class MemoryDelete(LoginRequiredMixin, DeleteView):
    model = Memory
    context_object_name = 'memory'
    success_url = reverse_lazy('memories')
