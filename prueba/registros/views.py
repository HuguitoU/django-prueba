from django.shortcuts import render
from .models import Alumnos
#Accedemos al modelo alumnos que contiene la estructura de la tabña

# Create your views here.
def registros(request):
    alumnos = Alumnos.objects.all()
    #all recupera todos los objetos del modelo (registros de la tabla alumnos)
    return render(request, "registros/principal.html", {'alumnos':alumnos})
    #indicamos el lugar donde se renderizara el resultado de esta vista y enviamos la lista de alumnos recuperados
    