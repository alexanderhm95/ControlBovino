# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import PersonalInfo



class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = ['cedula', 'telefono', 'nombre', 'apellido', 'email']
        labels = {
            'cedula': 'Cédula',
            'telefono': 'Teléfono',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'email': 'Correo Electrónico',
        }
        widgets = {
            'cedula': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Cédula'}),
            'telefono': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Teléfono'}),
            'nombre': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Apellido'}),
            'email': forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Correo Electrónico'}),
        }

    def __init__(self, *args, **kwargs):
        super(PersonalInfoForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'input'


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Contraseña'}))
    