from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .models import Task
from django.views.generic import ListView, DetailView, CreateView
from .forms import TaskForm
from django.urls import reverse_lazy


class Home(ListView):
    model = Task
    template_name = 'taskapp/home.html'
    context_object_name = 'tasks'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        return context

    # def get_queryset(self):
    #     return Task.objects.filter(is_completed=True)


class ViewTask(DetailView):
    model = Task
    template_name = 'taskapp/task.html'
    context_object_name = 'task'


class CreateTask(CreateView):
    form_class = TaskForm
    template_name = 'taskapp/add_task.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить задачу'
        return context


def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'taskapp/register.html', {'form':form})

def login(request):
    return render(request, 'taskapp/login.html')