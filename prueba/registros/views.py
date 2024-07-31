from django.shortcuts import render
from .models import Alumnos, ComentarioContacto, Archivos
from .forms import ComentarioContactoForm, FormArchivos
from django.contrib import messages
from django.shortcuts import get_object_or_404
import datetime
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

def mensajes(request):
    comentarios = ComentarioContacto.objects.all()
    return render(request, "registros/comentario.html", {'comentarios': comentarios})

def eliminarComentarioContacto(request, id,
    confirmacion = 'registros/confirmarEliminacion.html'):
    comentario = get_object_or_404(ComentarioContacto, id = id)
    if request.method == 'POST':
        comentario.delete()
        comentarios = ComentarioContacto.objects.all() 
        return render(request, "registros/comentario.html",
                      {'comentarios': comentarios})
    return render(request, confirmacion, {'object':comentario})

def formEditarComentario(request):
    return render(request, "registros/editarComentario.html")

def consultarComentarioIndividual(request, id):
    comentario = ComentarioContacto.objects.get(id=id)
    return render(request, "registros/formEditarComentario.html", {'comentario': comentario})

def editarComentarioContacto(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    form = ComentarioContactoForm(request.POST, instance = comentario)
    if form.is_valid():
        form.save()
        comentarios = ComentarioContacto.objects.all()
        return render(request, "registros/comentario.html", {'comentarios': comentarios})
    return render(request, "registros/formEditarComentario.html", {'comentario': comentario})

def consultar1(request):
    alumnos = Alumnos.objects.filter(carrera = "TI")
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar2(request):
    alumnos = Alumnos.objects.filter(carrera = "TI").filter(turno = "Matutino")
    return render(request, "registros/consultas.html",{'alumnos':alumnos})

def consultar3(request):
    alumnos = Alumnos.objects.all().only("matricula", "nombre", "carrera", "turno", "imagen")
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar4(request):
    alumnos = Alumnos.objects.filter(turno__contains = "Vesp")
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar5(request):
    alumnos = Alumnos.objects.filter(nombre__in = ["Juan", "Ana"])
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar6(request):
    fechaInicio = datetime.date(2024, 6, 27)
    fechaFin = datetime.date(2024, 8, 2)
    alumnos = Alumnos.objects.filter(created__range = (fechaInicio, fechaFin))
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar7(request):
    alumnos = Alumnos.objects.filter(comentario__coment__contains = 'No inscrito')
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def archivos(request):
    if request.method == 'POST':
        form = FormArchivos(request.POST, request.FILES)
        if form.is_valid():
            titulo = request.POST['titulo']
            descripcion = request.POST['descripcion']
            archivo = request.FILES['archivo']
            insert = Archivos(titulo = titulo, descripcion = descripcion, archivo = archivo)
            insert.save()
            return render(request, "registros/archivos.html")
        else:
            messages.error(request, "Error al procesar el formulario")
    else: 
        return render(request, "registros/archivos.html", {'archivo': Archivos})
    
def consultasSQL(request):
    alumnos = Alumnos.objects.raw('SELECT id, matricula, nombre, carrera, turno, imagen FROM registros_alumnos WHERE carrera = "TI" ORDER BY turno DESC')

    return render(request, "registros/consultas.html", {'alumnos': alumnos})
    