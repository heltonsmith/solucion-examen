
from django.urls import path
from .views import (
    index, 
    contacto, 
    login_user, logout_user, 
    registro, 
    cita, 
    ContactoCreateView,
    ContactoListView,
    UserProfileUpdateView,
    CreateAgendaView,
    AgendaListView)

urlpatterns = [
    path('', index, name="index"),
    path('contacto/', ContactoCreateView.as_view(), name="contacto"),
    path('contactos/', ContactoListView.as_view(), name="contactos"),
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name="logout"),
    path('registro/', registro, name="registro"),
    path('profile/edit/', UserProfileUpdateView.as_view(), name='profile_edit'),
    path('agenda/nueva/', CreateAgendaView.as_view(), name="agenda_nueva"),
    path('agendas', AgendaListView.as_view(), name="agendas"),
    path('agenda/<int:id>/cita', cita, name="cita"),
]
