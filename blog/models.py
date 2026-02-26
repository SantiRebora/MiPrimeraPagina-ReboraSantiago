from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Director(models.Model):
    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=250)
    nacionalidad = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    

class Genero(models.Model):
    nombre = models.CharField(max_length=250, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    
class Pelicula(models.Model):
    titulo = models.CharField(max_length=250)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    sinopsis = models.TextField()
    fecha_estreno = models.DateField()
    duracion = models.IntegerField(help_text="Duración total en minutos.")
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    puntuacion = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], blank=True, null=True)
