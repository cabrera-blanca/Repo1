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

    if request.method == "GET":
        nombre = request.GET['nombre']
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

def ver_alumnos(request):
    alumnos = Alumno.objects.all()
    dicc =  {"alumnos":alumnos }
    plantilla = loader.get_template("ver_alumnos.html")
    respuesta = plantilla.render(dicc)
    return HttpResponse(respuesta)

def alumno_formulario(request):

    if request.method == "POST":
    
        mi_formulario = Alumno_formulario(request.POST)
        
        if mi_formulario.is_valid(): 
            datos =  mi_formulario.cleaned_data
            alumno = Alumno( apellido=datos["apellido"] , nombre = datos["nombre"],dni =datos["dni"],email =datos["email"], fecha_nacimiento = datos ["fecha_nacimiento"])
            alumno.save()
            return render(request , "alta_alumnos.html")

    return render(request , "alta_alumnos.html")

def eliminar_alumno(request, id):
    Alumno.objects.get(id=id).delete()
    alumno = Alumno.objects.all()
    return render(request , "ver_alumnos.html", {"alumnos" :alumno})

def editar_alumno(request , id):
    alumno = Alumno.objects.get(id=id)

    if request.method == "POST":
        mi_formulario = Alumno_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            alumno.apellido = datos["apellido"]
            alumno.nombre = datos["nombre"]
            alumno.dni = datos["dni"]
            alumno.email = datos["email"]
            alumno.fecha_nacimiento = datos["fecha_nacimiento"]
            alumno.save()
            alumno = Alumno.objects.all()
            return render(request , "ver_alumnos.html" , {"alumno":alumno})
    else:
        mi_formulario = Alumno_formulario(initial={"nombre":alumno.nombre , "apellido":alumno.apellido, "dni": alumno.dni, "email": alumno.email, "fecha_nacimiento": alumno.fecha_nacimiento})

    return render( request , "editar_alumnos.html" , {"mi_formulario": mi_formulario , "alumno":alumno})

def buscar_alumno (request):
    return render(request, "busqueda_alumno.html")

def resultado_alumno(request):

    if request.method == "GET":
        dni = request.GET['dni']
        alumno = Alumno.objects.filter(dni__icontains=dni)
        return render(request,"resultado.alumno.html",{"alumnos" : alumno})    
    else :
        HttpResponse("Ingrese el nombre del curso")

# -----------Profesores---------- #
def profesores(request):
    return render (request , "profesores.html") 

def ver_profesores(request):
    profesores = Profesores.objects.all()
    dicc =  {"profesores":profesores }
    plantilla = loader.get_template("ver_profesores.html")
    respuesta = plantilla.render(dicc)
    return HttpResponse(respuesta)