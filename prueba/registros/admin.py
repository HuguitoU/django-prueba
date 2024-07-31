from django.contrib import admin
from .models import Alumnos, Comentario, ComentarioContacto, Archivos

# Register your models here.
class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('matricula', 'nombre', 'carrera', 'turno') #Visualizacion
    search_fields = ('matricula', 'nombre', 'carrera', 'turno') #Barra de 
    date_hierarchy = 'created'
    list_filter = ('carrera', 'turno')
    list_per_page = 2
    list_display_links = ('matricula', 'nombre')
    list_editable = ('turno',)

    def get_readonly_fields(self, request, obj = None):
        if request.user.groups.filter(name = "Usuarios").exists():
            return('matricula', 'carrera', 'turno')
        else:
            return('created','updated')

admin.site.register(Alumnos, AdministrarModelo)

class AdministrarComentarios(admin.ModelAdmin):
    list_display = ('id', 'coment')
    search_fields = ('id', 'created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')

admin.site.register(Comentario, AdministrarComentarios)

class AdministrarComentariosContacto(admin.ModelAdmin):
    list_display = ('id', 'mensaje')
    search_fields = ('id', 'created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')

admin.site.register(ComentarioContacto, AdministrarComentariosContacto)


class AdministrarArchivos(admin.ModelAdmin):
    list_display = ('id', 'titulo')

admin.site.register(Archivos, AdministrarArchivos)