from django import forms
from .models import Task
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Имя пользователя',
        widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "Имя пользователя"})
    )
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': "Пароль"}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label='Имя пользователя',
        widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "Имя пользователя"})
    )
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': "Пароль"}))
    password2 = forms.CharField(label='Подтверждение пароля',
                                widget=forms.PasswordInput(
                                    attrs={'class': "form-control", 'placeholder': "Подтверждение пароля"}))

    email = forms.EmailField(label='Email',
                             widget=forms.EmailInput(attrs={'class': "form-control", 'placeholder': "Email"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'photo')
        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control", 'placeholder': "Заголовок"}),
            'description': forms.Textarea(attrs={'class': "form-control", 'placeholder': "Описание"}),
        }
