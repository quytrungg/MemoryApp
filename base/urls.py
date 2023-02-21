from django.urls import path
from .views import MemoryList, MemoryDetail

urlpatterns = [
    path('', MemoryList.as_view(), name='memories'),
    path('memory/<int:pk>', MemoryDetail.as_view(), name='memory')
]