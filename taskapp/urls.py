from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('task/<int:task_id>/', get_task, name='task'),
]
