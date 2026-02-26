from django.contrib import admin
from .models import Genero, Director, Pelicula

admin.site.register(Director)
admin.site.register(Genero)
admin.site.register(Pelicula)
