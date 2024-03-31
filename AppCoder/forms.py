from django import forms
from django.db  import models
from AppCoder.models import *

#--Cursos

class Curso_formulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    camada = forms.IntegerField()
    
#-------------------------------------------------------------

#--Alumnos

class Alumno_formulario(forms.Form):

    apellido = forms.CharField(max_length=256)
    nombre = forms.CharField(max_length=256)
    dni = forms.CharField(max_length=9)
    email = forms.EmailField(required=True)
    fecha_nacimiento = forms.DateField(required=True)
    # curso = forms.ChoiceField(choices=(models.ForeignKey(Curso, on_delete=models.SET_NULL, blank=True, null=True)), required=True, label="Seleccione su curso")

#-------------------------------------------------------------

#--Profesores   
    


