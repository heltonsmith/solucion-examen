from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def contacto(request):
    return render(request, "contacto.html")

def login(request):
    return render(request, "login.html")

def registro(request):
    return render(request, "registro.html")

def agenda_nueva(request):
    return render(request, "agenda.html")

def agendas(request):
    return render(request, "agendas.html")

def cita(request):
    return render(request, "cita.html")