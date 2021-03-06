from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, redirect

from .models import Task
from django.views.generic import ListView, DetailView, CreateView
from .forms import TaskForm, UserRegisterForm, UserLoginForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(ListView):
    model = Task
    template_name = 'taskapp/home.html'
    context_object_name = 'tasks'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        return context

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user:
                queryset = Task.objects.filter(author=self.request.user)
                return queryset
        return Task.objects.none()


class ViewTask(LoginRequiredMixin,DetailView):
    model = Task
    template_name = 'taskapp/task.html'
    context_object_name = 'task'


class CreateTask(LoginRequiredMixin,CreateView):
    form_class = TaskForm
    template_name = 'taskapp/add_task.html'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить задачу'
        return context

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return redirect('home')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'taskapp/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()

    return render(request, 'taskapp/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')
