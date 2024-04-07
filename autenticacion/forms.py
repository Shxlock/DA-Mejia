from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    direccion = forms.CharField(max_length=100)  # Nuevo campo 'direccion'

    class Meta:
        model = User
        fields = ("first_name", "last_name","username", "password1", "password2", "email","direccion"  )