from django.urls import path
from .views import MemoryList, MemoryDetail, MemoryCreate, MemoryUpdate, MemoryDelete, CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('', MemoryList.as_view(), name='memories'),
    path('memory/<int:pk>', MemoryDetail.as_view(), name='memory'),
    path('memory-create/', MemoryCreate.as_view(), name='memory-create'),
    path('memory-update/<int:pk>', MemoryUpdate.as_view(), name='memory-update'),
    path('memory-delete/<int:pk>', MemoryDelete.as_view(), name='memory-delete'),
]