from django.shortcuts import render, redirect
from .forms import ContactoForm, UserRegistrationForm
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Contacto
from django.views.generic import CreateView, ListView


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

def login(request):
    return render(request, "login.html")

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

def agenda_nueva(request):
    return render(request, "agenda.html")

def agendas(request):
    return render(request, "agendas.html")

def cita(request):
    return render(request, "cita.html")