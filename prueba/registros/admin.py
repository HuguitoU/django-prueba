from django.contrib import admin
from .models import Alumnos
from .models import Comentario
from .models import ComentarioContacto

# Register your models here.
class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('matricula', 'nombre', 'carrera', 'turno') #Visualizacion
    search_fields = ('matricula', 'nombre', 'carrera', 'turno') #Barra de 
    date_hierarchy = 'created'
    list_filter = ('carrera', 'turno')

admin.site.register(Alumnos, AdministrarModelo)

class AdministrarComentarios(admin.ModelAdmin):
    list_display = ('id', 'alumno', 'coment')
    search_fields = ('id', 'created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')

admin.site.register(Comentario, AdministrarComentarios)

class AdminComentarioContacto(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'mensaje')
    search_fields = ('usuario',)
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')

admin.site.register(ComentarioContacto, AdminComentarioContacto)



