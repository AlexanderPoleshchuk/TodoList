from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('task/<int:pk>/', ViewTask.as_view(), name='task'),
    path('task/add-task/', CreateTask.as_view(), name='add_task'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
