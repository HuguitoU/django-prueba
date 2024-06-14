from django.contrib import admin
from .models import Alumnos

# Register your models here.
class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('matricula', 'nombre', 'carrera', 'turno') #Visualizacion
    search_fields = ('matricula', 'nombre', 'carrera', 'turno') #Barra de 
    date_hierarchy = 'created'
    list_filter = ('carrera', 'turno')

admin.site.register(Alumnos, AdministrarModelo)

