from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth.models import User
import math


class Task(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    description = models.TextField(blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_completed = models.BooleanField(default=False, verbose_name='Выполнено', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', default=None)

    def get_absolute_url(self):
        return reverse_lazy('task', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача(y)'
        verbose_name_plural = 'Задачи'
        ordering = ['-created_at']
