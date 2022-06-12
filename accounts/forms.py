from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.forms import widgets

from .models import User


class AccountCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(AccountCreateForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget = widgets.EmailInput(attrs={'placeholder': 'Email'})
        self.fields['first_name'].widget = widgets.TextInput(attrs={'placeholder': 'First name'})
        self.fields['last_name'].widget = widgets.TextInput(attrs={'placeholder': 'Last name'})
        self.fields['password1'].widget = widgets.PasswordInput(attrs={'placeholder': 'New password'})
        self.fields['password2'].widget = widgets.PasswordInput(attrs={'placeholder': 'Repeat password'})

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username or Email')


class AccountChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password']


class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
