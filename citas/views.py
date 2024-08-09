from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .forms import (ContactoForm, 
                    UserRegistrationForm, LoginForm, 
                    UserUpdateForm, ProfileUpdateForm, 
                    CustomPasswordChangeForm, AgendaForm)
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Contacto, Profile, Agenda, CentroMedico, Especialista
from django.views.generic import CreateView, ListView, View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from collections import OrderedDict

# Create your views here.
def index(request):
    return render(request, "index.html")

'''
    CONTACTO CON FUNCION Y CON CLASE
'''
def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Tu mensaje ha sido enviado con éxito!')
            return redirect('contacto')
    else:
        form = ContactoForm()
    return render(request, "contacto.html", {'form': form}) 

class ContactoCreateView(CreateView):
    model = Contacto
    form_class = ContactoForm
    template_name = 'contacto.html'
    success_url = reverse_lazy('contacto')  # URL a la que se redirigirá después del éxito

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, '¡Tu mensaje ha sido enviado con éxito!')
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        # Puedes agregar lógica adicional aquí si es necesario
        return response
    
class ContactoListView(ListView):
    model = Contacto
    template_name = 'contacto_list.html'
    context_object_name = 'lista_contactos' #lista_contactos=Contacto.objects.all()
    paginate_by = 4  # Opcional: Número de contactos por página
'''
    FIN - CONTACTO CON FUNCION Y CON CLASE
'''    

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirigir a una página después del inicio de sesión exitoso
                return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def registro(request):
    mensaje = ''
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            mensaje = '¡Registro exitoso! Ahora puedes iniciar sesión.'
    else:
        form = UserRegistrationForm()
    return render(request, 'registro.html', {'form': form, 'mensaje': mensaje})

def logout_user(request):
    logout(request)
    return render(request, "logout.html")

def cita(request, id):
    try:
        agenda = get_object_or_404(Agenda, id=id)
        # Lógica de la vista
        return render(request, 'cita.html', {'agenda': agenda})
    except Http404:
        return render(request, 'cita.html', {'message': 'No existe cita'})

'''
    Edit User
'''
class UserProfileUpdateView(LoginRequiredMixin, View):
    template_name = 'profile_update.html'

    def get(self, request, *args, **kwargs):
        user_form = UserUpdateForm(instance=request.user)
        profile = Profile.objects.get(user=request.user)
        profile_form = ProfileUpdateForm(instance=profile)
        password_form = CustomPasswordChangeForm(user=request.user)
        
        return render(request, self.template_name, {
            'user_form': user_form,
            'profile_form': profile_form,
            'password_form': password_form,
        })

    def post(self, request, *args, **kwargs):
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile = Profile.objects.get(user=request.user)
        profile_form = ProfileUpdateForm(request.POST, instance=profile)
        password_form = CustomPasswordChangeForm(user=request.user, data=request.POST)

        if user_form.is_valid() and profile_form.is_valid() and password_form.is_valid():
            user_form.save()
            profile_form.save()
            user = password_form.save()
            update_session_auth_hash(request, user)  # Mantener la sesión activa
            return redirect('index')  # Redirige después de éxito

        return render(request, self.template_name, {
            'user_form': user_form,
            'profile_form': profile_form,
            'password_form': password_form,
        })
'''
    Fin Edit User
'''


class CreateAgendaView(View):
    template_name = 'agenda.html'
    
    def get(self, request, *args, **kwargs):
        form = AgendaForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = AgendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agendas')  # Redirige a una página de éxito o lista de agendas
        
        return render(request, self.template_name, {'form': form})
    

class AgendaListView(ListView):
    model = Agenda
    template_name = 'agendas.html'
    context_object_name = 'agendas'
    paginate_by = 2  

    def get_queryset(self):
        queryset = super().get_queryset()

        centro_id = self.request.GET.get('centro_medico')
        especialista_id = self.request.GET.get('especialidad')

        if centro_id and centro_id != '0':
            queryset = queryset.filter(centro_medico_id=centro_id)

        if especialista_id and especialista_id != '0':
            especialidad = Especialista.objects.get(id=especialista_id).especialidad
            queryset = queryset.filter(especialista__especialidad=especialidad)

        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['centros'] = CentroMedico.objects.all()

        especialistas = Especialista.objects.all()

        especialistas_unicos = OrderedDict()

        for especialista in especialistas:
            if especialista.especialidad not in especialistas_unicos:
                especialistas_unicos[especialista.especialidad] = especialista

        especialistas_unicos_list = list(especialistas_unicos.values())
        context['especialidades'] = especialistas_unicos_list

        return context
