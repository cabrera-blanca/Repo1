from datetime import *
from django.db import models

# Create your models here.

#-----Cursos-------#
class Curso (models.Model):
    nombre = models.CharField(max_length = 100)
    camada = models.IntegerField()


    def __str__(self):
        return  f"Curso : {self.nombre}, Camada : {self.camada}"
    

#-----Alumnos-------#
class Alumno (models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    dni = models.IntegerField()
    email = models.EmailField()
    fecha_nacimiento = models.DateField( blank=True, null=True)
    # curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, blank=True, null=True)

        
    def __str__(self):
        return f'Alumno : {self.apellido} {self.nombre}'


#-----Profesores------#
class Profesores(models.Model):
    apellido = models.CharField(max_length=256, default="")
    nombre = models.CharField(max_length=256)
    curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return  f'Profesor: {self.apellido} {self.nombre}, {self.curso}'
            
    