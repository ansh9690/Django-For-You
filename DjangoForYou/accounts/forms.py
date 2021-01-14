from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class': 'form-control'
    }))
    email = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Email',
        'class': 'form-control'
    }))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'form-control',
        'title': 'Password'
    }))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'placeholder': 'Password Confirmation',
        'class': 'form-control',
        'title': 'Password'
    }))
    
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Password Confirmation"
        
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        