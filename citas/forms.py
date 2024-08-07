from .models import Contacto
from django import forms

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = ('nombre', 'email', 'mensaje')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Mensaje'}),
        }

