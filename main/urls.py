from django.urls import path
from .views import *


urlpatterns = [
    path('get_tasks/', get_tasks),
    path('create_task/', create_task),
    path('update_task/<int:pk>/', update_task),
    path('delete_task/<int:pk>/', delete_task)
]