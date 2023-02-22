from django.urls import path
from .views import MemoryList, MemoryDetail, MemoryCreate, MemoryUpdate

urlpatterns = [
    path('', MemoryList.as_view(), name='memories'),
    path('memory/<int:pk>', MemoryDetail.as_view(), name='memory'),
    path('memory-create/', MemoryCreate.as_view(), name='memory-create'),
    path('memory-update/<int:pk>', MemoryUpdate.as_view(), name='memory-update'),
]