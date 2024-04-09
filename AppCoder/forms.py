from django import forms
from django.db  import models
from AppCoder.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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

class UserEditForm(UserCreationForm):
    email = forms.EmailField(help_text="Required. Inform a valid email address.", label=("E-mail"))
    password1 = forms.CharField(label=("Password"), widget= forms.PasswordInput, help_text='Use at least one letter, one number and one special')
    password2 = forms.CharField(label=("Confirm password"), widget= forms.PasswordInput , help_text='Enter the same password as before, for verification.')

    class Meta:
        model =  User
        fields = ('email','password1', 'password2')
        help_text ={k:"" for k in fields}

#-----------------------------------------------------

#--Profesores   
    


