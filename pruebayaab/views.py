from django.shortcuts import render
from .forms import Formularioyaab


# Create your views here.
def vista_formulario(request):
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
