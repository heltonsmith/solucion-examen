from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contacto(models.Model):
    nombre = models.CharField('Nombre Contacto', max_length=100)
    email = models.EmailField('Email Contacto', max_length=200)
    mensaje = models.TextField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Username: {self.email} \n Mensaje: {self.mensaje}"
    

class Profile(models.Model):
    TIPO_USUARIO = [
        ('paciente', 'Paciente'),
        ('administrador', 'Administrador'),
    ]
     
    tipo_usuario = models.CharField(choices=TIPO_USUARIO, max_length=20, default='Paciente')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return "Username: " + self.user.username + " Tipo Usuario: " + self.tipo_usuario
    
class Especialista(models.Model):
    nombre = models.CharField('Nombre especialista', max_length=200)
    especialidad = models.CharField('Especialidad', max_length=200)

    def __str__(self):
        return "Nombre: " + self.nombre + " - Especialidad: " + self.especialidad


class CentroMedico(models.Model):
    nombre = models.CharField('Nombre centro', max_length=200)
    direccion = models.CharField('Dirección', max_length=200)

    def __str__(self):
        return "Nombre: " + self.nombre + " - Dirección: " + self.direccion
    

class Agenda(models.Model):
    fecha_disponible = models.DateField('Fecha Disponible', auto_now=False, auto_now_add=False)
    hora_disponible = models.TimeField('Hora Disponible', auto_now=False, auto_now_add=False)
    especialista = models.ForeignKey(Especialista, on_delete=models.CASCADE)
    centro_medico = models.ForeignKey(CentroMedico, on_delete=models.CASCADE)

    def __str__(self):
        return "Agenda: " + str(self.fecha_disponible) + " - Hora: " + str(self.hora_disponible) + " - Especialista: " + self.especialista.nombre + " - Centro: " + self.centro_medico.nombre