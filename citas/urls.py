
from django.urls import path
from .views import (
    index, 
    contacto, 
    login, 
    registro, 
    agenda_nueva, 
    agendas, 
    cita, 
    ContactoCreateView,
    ContactoListView)

urlpatterns = [
    path('', index, name="index"),
    path('contacto/', ContactoCreateView.as_view(), name="contacto"),
    path('contactos/', ContactoListView.as_view(), name="contactos"),
    path('login/', login, name="login"),
    path('registro/', registro, name="registro"),
    path('agenda/nueva/', agenda_nueva, name="agenda_nueva"),
    path('agendas', agendas, name="agendas"),
    path('agenda/id/cita', cita, name="cita"),
]
