from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Director, Genero, Pelicula

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "apellido": forms.TextInput(attrs={"class": "form-control"}),
            "nacionalidad": forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Ej: Argentina, España, EEUU..."
    }
),}

class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Breve descripción del género..."
            }),
        }

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = "__all__"
        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control"}),
            "genero": forms.Select(attrs={"class": "form-select"}),
            "sinopsis": forms.Textarea(attrs={"class": "form-control"}),
            "fecha_estreno": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "duracion": forms.NumberInput(attrs={"class": "form-control"}),
            "director": forms.Select(attrs={"class": "form-select"}),
            "puntuacion": forms.Select(choices=[
                    (1, "⭐"),
                    (2, "⭐⭐"),
                    (3, "⭐⭐⭐"),
                    (4, "⭐⭐⭐⭐"),
                    (5, "⭐⭐⭐⭐⭐"),
                ],
                attrs={"class": "form-select"},
            ),
        }

class BusquedaPeliculaForm(forms.Form):
    titulo = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    genero = forms.ModelChoiceField(
        queryset=Genero.objects.all(),
        required=False,
        widget=forms.Select(attrs={"class": "form-select"}))
    puntuacion_minima = forms.ChoiceField(
        required=False,
        choices=[
            ("", "Cualquiera"),
            (1, "⭐"),
            (2, "⭐⭐"),
            (3, "⭐⭐⭐"),
            (4, "⭐⭐⭐⭐"),
            (5, "⭐⭐⭐⭐⭐"),
        ],
        widget=forms.Select(attrs={"class": "form-select"}))


    


