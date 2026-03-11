from django.contrib import admin
from django.urls import path
from blog import views
from .models import Pelicula, Director, Genero
from django.contrib.auth.views import LoginView, LogoutView

app_name = "blog"

urlpatterns = [
    path("", views.PeliculaListView.as_view(), name="pelicula_list"),
    path("peliculas/<int:pk>/", views.PeliculaDetailView.as_view(), name="pelicula_detail"),
    path("peliculas/nueva/", views.PeliculaCreateView.as_view(), name="pelicula_create"),
    path("peliculas/<int:pk>/editar/", views.PeliculaUpdateView.as_view(), name="pelicula_update"),
    path("peliculas/<int:pk>/eliminar/", views.PeliculaDeleteView.as_view(), name="pelicula_delete"),

    path("generos/", views.GeneroListView.as_view(), name="genero_list"),
    path("generos/nuevo/", views.GeneroCreateView.as_view(), name="genero_create"),
    path("generos/<int:pk>/editar/", views.GeneroUpdateView.as_view(), name="genero_update"),
    path("generos/<int:pk>/eliminar/", views.GeneroDeleteView.as_view(), name="genero_delete"),

    path("directores/", views.DirectorListView.as_view(), name="director_list"),
    path("directores/nuevo/", views.DirectorCreateView.as_view(), name="director_create"),
    path("directores/<int:pk>/editar/", views.DirectorUpdateView.as_view(), name="director_update"),
    path("directores/<int:pk>/eliminar/", views.DirectorDeleteView.as_view(), name="director_delete"),

    path("login/", LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="blog:pelicula_list"), name="logout"),
    path("registro/", views.RegistroView.as_view(), name="registro"),
]