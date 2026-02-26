from django.contrib import admin
from django.urls import path
from blog import views


from .models import Pelicula, Director, Genero

app_name = "blog"

urlpatterns = [
    path("", views.PeliculaListView.as_view(), name="pelicula-list"),
    path("pelicula/<int:pk>/", views.PeliculaDetailView.as_view(), name="pelicula-detail"),
    path("pelicula/nueva/", views.PeliculaCreateView.as_view(), name="pelicula-create"),
    path("pelicula/<int:pk>/editar/", views.PeliculaUpdateView.as_view(), name="pelicula-update"),
    path("pelicula/<int:pk>/eliminar/", views.PeliculaDeleteView.as_view(), name="pelicula-delete"),
    path("generos/", views.GeneroListView.as_view(), name="genero-list"),
    path("genero/nuevo/", views.GeneroCreateView.as_view(), name="genero-create"),
    path("directores/", views.DirectorListView.as_view(), name="director-list"),
    path("director/nuevo/", views.DirectorCreateView.as_view(), name="director-create"),
]