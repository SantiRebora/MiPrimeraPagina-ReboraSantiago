from django.contrib import admin
from .models import Pelicula, Director, Genero

class PeliculaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "director", "genero", "fecha_estreno", "puntuacion")
    search_fields = ("titulo",)
    list_filter = ("genero", "director", "fecha_estreno")
    ordering = ("-fecha_estreno",)


class DirectorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "nacionalidad")
    search_fields = ("nombre", "apellido")
    ordering = ("apellido",)


class GeneroAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)

admin.site.register(Pelicula, PeliculaAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Genero, GeneroAdmin)