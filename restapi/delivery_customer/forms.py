from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class RegisterForms(forms.ModelForm):

    class RegisterUserForm(UserCreationForm):
        username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input', 'value placeholder': 'Логин'}))
        email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input', 'value placeholder': 'Email адрес'}))
        password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input', 'value placeholder': 'Пароль'}))
        password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input', 'value placeholder': 'Повтор пароля'}))

        class Meta:
            model = User
            fields = ('username', 'email', 'password1', 'password2')

    class LoginUserForm(AuthenticationForm):
        username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control', 'value placeholder': 'Логин'}))
        password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', 'value placeholder': 'Пароль'}))