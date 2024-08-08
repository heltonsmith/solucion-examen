from django.contrib import admin
from .models import Contacto, Profile, Especialista, CentroMedico, Agenda

# Register your models here.
admin.site.register(Contacto)
admin.site.register(Profile)
admin.site.register(Especialista)
admin.site.register(CentroMedico)
admin.site.register(Agenda)