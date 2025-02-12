from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import Formularioyaab
from django.contrib.auth.decorators import login_required, user_passes_test


def vista_formulario(request): #solicito esta respuesta para el usuario
    
    if request.method == 'POST':
        form = Formularioyaab(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']
            telefonico = form.cleaned_data['telefonico']
            #Enviar una respuesta al usuario
        return render(request, 'pruebayaab/mensaje.html', {'nombre': nombre})

    else:
        form = Formularioyaab()
    return render (request, 'pruebayaab/formulario.html', {'form': form})


def landing(request):
    return render(request, 'pruebayaab/landing.html')

def es_superuser(user):
    return user.is_superuser

@login_required
@user_passes_test(es_superuser, login_url='/')
def dashboard(request):
    if not request.user.is_superuser:
        return redirect('landing')
    return render(request, 'pruebayaab/dashboard.html')

def login_view(request):
    return render(request, "pruebayaab/login.html")

