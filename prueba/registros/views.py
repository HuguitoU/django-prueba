from django.shortcuts import render
from .models import Alumnos
from .forms import ComentarioContactoForm
#Accedemos al modelo alumnos que contiene la estructura de la tabña

# Create your views here.
def registros(request):
    alumnos = Alumnos.objects.all()
    #all recupera todos los objetos del modelo (registros de la tabla alumnos)
    return render(request, "registros/principal.html", {'alumnos':alumnos})
    #indicamos el lugar donde se renderizara el resultado de esta vista y enviamos la lista de alumnos recuperados
    
def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registros/contacto.html')
    form = ComentarioContactoForm()
    return render(request, 'registros/contacto.html', {'form': form})

def contacto(request):
    return render(request, "registros/contacto.html")