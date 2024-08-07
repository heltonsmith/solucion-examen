from django.db import models

# Create your models here.
class Contacto(models.Model):
    nombre = models.CharField('Nombre Contacto', max_length=100)
    email = models.EmailField('Email Contacto', max_length=200)
    mensaje = models.TextField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Email: {self.email} \n Mensaje: {self.mensaje}"