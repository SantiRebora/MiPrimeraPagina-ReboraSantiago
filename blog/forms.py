from django import forms
from .models import Director, Genero, Pelicula

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = "__all__"

class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = "__all__"

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = "__all__"


class BusquedaPeliculaForm(forms.Form):
    titulo = forms.CharField(required=False)
    genero = forms.ModelChoiceField(queryset=Genero.objects.all(), required=False)
    puntuacion_minima = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], required=False)


    


