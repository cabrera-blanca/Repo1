from django.shortcuts import redirect, render
from AppCoder.models import *
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import *

# -----------VIEWS---------- #

# -----------Home---------- #
def inicio (request):
    return render(request, "padre.html")

# -----------Cursos---------- #

def ver_cursos (request):
    cursos = Curso.objects.all()
    dicc =  {"cursos":cursos }
    plantilla = loader.get_template("ver_cursos.html")
    respuesta = plantilla.render(dicc)
    return HttpResponse(respuesta)

def curso_formulario(request):

    if request.method == "POST":

        mi_formu = Curso_formulario (request.POST)
        
        if mi_formu.is_valid(): 
            datos =  mi_formu.cleaned_data
            curso = Curso( nombre=datos["nombre"] , camada=datos["camada"])
            curso.save()
            return render(request , "formulario.html")

    return render(request , "formulario.html")

def buscar_curso (request):
    return render(request, "buscar_curso.html")

def buscar(request):

    if request.get["nombre"]:
        nombre = request.get["nombre"]
        cursos = Curso.objects.filter(nombre__icontains=nombre)
        return render(request,"busqueda.html",{"cursos" : cursos})    
    else :
        HttpResponse("Ingrese el nombre del curso")

def eliminar_curso(request, id):
    Curso.objects.get(id=id).delete()
    curso = Curso.objects.all()
    return render(request , "ver_cursos.html", {"cursos" :curso})

def editar_curso(request , id):
    curso = Curso.objects.get(id=id)

    if request.method == "POST":
        mi_formulario = Curso_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso.nombre = datos["nombre"]
            curso.camada = datos["camada"]
            curso.save()
            curso = Curso.objects.all()
            return render(request , "ver_cursos.html" , {"cursos":curso})
    else:
        mi_formulario = Curso_formulario(initial={"nombre":curso.nombre , "camada":curso.camada})

    return render( request , "editar_curso.html" , {"mi_formulario": mi_formulario , "curso":curso})

# -----------Alumnos---------- #

def alumnos (request):
    return render (request , "alumnos.html") 


# -----------Profesores---------- #