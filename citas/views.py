from django.shortcuts import render, redirect
from .forms import (ContactoForm, 
                    UserRegistrationForm, LoginForm, 
                    UserUpdateForm, ProfileUpdateForm, 
                    CustomPasswordChangeForm, AgendaForm)
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Contacto, Profile, Agenda
from django.views.generic import CreateView, ListView, View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin

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

def cita(request):
    return render(request, "cita.html")

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


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Aquí puedes añadir datos adicionales al contexto si es necesario
        return context