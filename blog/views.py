from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from . import forms
from .models import Director, Genero, Pelicula
from .forms import DirectorForm, GeneroForm, PeliculaForm, BusquedaPeliculaForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

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

class PeliculaCreateView(LoginRequiredMixin, CreateView):
    model = Pelicula
    form_class = PeliculaForm
    success_url = reverse_lazy("blog:pelicula_list")

    def get_initial(self):
        initial = super().get_initial()

        genero_id = self.request.GET.get("genero")
        director_id = self.request.GET.get("director")

        if genero_id:
            initial["genero"] = genero_id

        if director_id:
            initial["director"] = director_id

        return initial
    
class PeliculaUpdateView(UpdateView):
    model = Pelicula
    form_class = PeliculaForm
    template_name = "blog/pelicula_form.html"
    success_url = reverse_lazy("blog:pelicula_list")

class PeliculaDeleteView(DeleteView):
    model = Pelicula
    template_name = "blog/pelicula_confirm_delete.html"
    success_url = reverse_lazy("blog:pelicula_list")

class GeneroListView(ListView):
    model = Genero
    template_name = "blog/genero_list.html"
    context_object_name = "generos"

class GeneroCreateView(CreateView):
    model = Genero
    form_class = GeneroForm

    def form_valid(self, form):
        self.object = form.save()  

        next_url = self.request.GET.get("next")
        if next_url:
            return redirect(next_url)

        return redirect("pelicula_list")

class GeneroUpdateView(UpdateView):
    model = Genero
    fields = ["nombre"]
    template_name = "blog/genero_form.html"
    success_url = reverse_lazy("blog:genero_list")

class GeneroDeleteView(DeleteView):
    model = Genero
    template_name = "blog/genero_confirm_delete.html"
    success_url = reverse_lazy("blog:genero_list")

class DirectorListView(ListView):
    model = Director
    template_name = "blog/director_list.html"
    context_object_name = "directores"

class DirectorCreateView(CreateView):
    model = Director
    fields = ["nombre", "apellido", "nacionalidad"]
    template_name = "blog/director_form.html"

    def form_valid(self, form):
        self.object = form.save()  

        next_url = self.request.GET.get("next")
        if next_url:
            return redirect(next_url)

        return redirect("pelicula_list")

class DirectorUpdateView(UpdateView):
    model = Director
    fields = ["nombre", "apellido", "nacionalidad"]
    template_name = "blog/director_form.html"
    success_url = reverse_lazy("blog:director_list")

class DirectorDeleteView(DeleteView):
    model = Director
    template_name = "blog/director_confirm_delete.html"
    success_url = reverse_lazy("blog:director_list")

class RegistroView(CreateView):
    form_class = UserCreationForm
    template_name = "blog/registro.html"
    success_url = reverse_lazy("blog:login")

