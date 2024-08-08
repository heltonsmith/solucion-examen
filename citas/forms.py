from .models import Contacto, Profile, Agenda
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm


class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = ('nombre', 'email', 'mensaje')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Mensaje'}),
        }

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        if commit:
            user.save()
            # Crear el perfil con el tipo de usuario por defecto 'Paciente'
            Profile.objects.create(user=user)
        return user
    
class LoginForm(AuthenticationForm):
    #username = forms.EmailField(label='Email')

    class Meta:
        model = User
        fields = ['username', 'password']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Clave'}),
        }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']  # Excluye el campo de contraseña aquí

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['tipo_usuario']

class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['password1', 'password2']  # PasswordChangeForm maneja esto automáticamente

class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = ['fecha_disponible', 'hora_disponible', 'especialista', 'centro_medico']
        widgets = {
            'fecha_disponible': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'hora_disponible': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'especialista': forms.Select(attrs={'class': 'form-control'}),
            'centro_medico': forms.Select(attrs={'class': 'form-control'}),
        }