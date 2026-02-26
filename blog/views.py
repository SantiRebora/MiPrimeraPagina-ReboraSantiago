from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import forms
from .models import Director, Genero, Pelicula
from .forms import DirectorForm, GeneroForm, PeliculaForm, BusquedaPeliculaForm


class PeliculaListView(ListView):
    model = Pelicula
    template_name = "blog/pelicula_list.html"
    context_object_name = "peliculas"

    def get_queryset(self):
        queryset = super().get_queryset()
        
        titulo = self.request.GET.get("titulo")
        genero = self.request.GET.get("genero")
        puntuacion_minima = self.request.GET.get("puntuacion_minima")

        if titulo:
            queryset = queryset.filter(titulo__icontains=titulo)

        if genero:
            queryset = queryset.filter(genero__id=genero)

        if puntuacion_minima:
            queryset = queryset.filter(puntuacion__gte=puntuacion_minima)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = BusquedaPeliculaForm(self.request.GET)
        return context
    
class PeliculaDetailView(DetailView):
    model = Pelicula
    template_name = "blog/pelicula_detail.html"
    context_object_name = "pelicula"

class PeliculaCreateView(CreateView):
    model = Pelicula
    form_class = PeliculaForm
    template_name = "blog/pelicula_form.html"
    success_url = reverse_lazy("blog:pelicula-list")

class PeliculaUpdateView(UpdateView):
    model = Pelicula
    form_class = PeliculaForm
    template_name = "blog/pelicula_form.html"
    success_url = reverse_lazy("blog:pelicula-list")

class PeliculaDeleteView(DeleteView):
    model = Pelicula
    template_name = "blog/pelicula_confirm_delete.html"
    success_url = reverse_lazy("blog:pelicula-list")

class GeneroListView(ListView):
    model = Genero
    template_name = "blog/genero_list.html"
    context_object_name = "generos"

class GeneroCreateView(CreateView):
    model = Genero
    form_class = GeneroForm
    template_name = "blog/genero_form.html"
    success_url = reverse_lazy("blog:genero-list")

class DirectorListView(ListView):
    model = Director
    template_name = "blog/director_list.html"
    context_object_name = "directores"

class DirectorCreateView(CreateView):
    model = Director
    form_class = DirectorForm
    template_name = "blog/director_form.html"
    success_url = reverse_lazy("blog:director-list")

