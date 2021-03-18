from django.shortcuts import render
from .models import Task
from django.views.generic import ListView, DetailView

# Create your views here.
class Home(ListView):
    model = Task
    template_name = 'taskapp/home.html'
    context_object_name = 'tasks'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        return context


def get_task(request, task_id):
    task = Task.objects.get(pk = task_id)
    return render(request, template_name='taskapp/task.html', context={'task': task})