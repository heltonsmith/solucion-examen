from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contacto(models.Model):
    nombre = models.CharField('Nombre Contacto', max_length=100)
    email = models.EmailField('Email Contacto', max_length=200)
    mensaje = models.TextField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Email: {self.email} \n Mensaje: {self.mensaje}"
    

class Profile(models.Model):
    TIPO_USUARIO = [
        ('paciente', 'Paciente'),
        ('administrador', 'Administrador'),
    ]
     
    tipo_usuario = models.CharField(choices=TIPO_USUARIO, max_length=20, default='Paciente')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return "Email: " + self.user.email + " Tipo Usuario: " + self.tipo_usuario