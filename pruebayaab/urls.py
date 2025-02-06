from django.urls import path
from .views import vista_formulario

urlpatterns = [
    path('formulario/', vista_formulario, name='formulario'),
]