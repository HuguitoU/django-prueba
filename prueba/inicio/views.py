from django.shortcuts import render, HttpResponse
menu = """
    <a href = "/">Home</a>
    <a href = "contacto/">Contacto</a>
"""
    
# Create your views here.
def principal(request):
    return render(request, "inicio/principal.html")

# Pagina de contacto
def contacto(request):
    return render(request, "inicio/contacto.html")

def formulario(request):
    return render(request, "inicio/formulario.html")

def ejemplo(request):
    return render(request, "inicio/ejemplo.html")

def seguridad(request, nombre = None):
    nombre = request.GET.get('nombre')
    return render(request, "inicio/seguridad.html", {'nombre': nombre})