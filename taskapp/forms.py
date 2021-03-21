from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'photo')
        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control", 'placeholder': "Заголовок"}),
            'description': forms.Textarea(attrs={'class': "form-control", 'placeholder': "Описание"}),
        }
