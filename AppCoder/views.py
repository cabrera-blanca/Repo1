from django.shortcuts import redirect, render
from AppCoder.models import *
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import *
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

# -----------VIEWS---------- #

# -----------Home---------- #
def inicio (request):
    avatares = Avatar.objects.filter(user=request.user.id)
    user = request.user.id
    if user is None:
        return render(request, "padre.html")
    else:
        return render(request, "padre.html", {"url":avatares[0].imagen.url})
    
# -----------Cursos---------- #
@login_required
def ver_cursos (request):
    cursos = Curso.objects.all()
    avatares = Avatar.objects.filter(user=request.user.id)
    user = request.user.id
    if user is None:
        return render(request, "ver_cursos.html")
    else:
        return render(request, "ver_cursos.html", {"url":avatares[0].imagen.url,"cursos": cursos })
    

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
    avatares = Avatar.objects.filter(user=request.user.id)
    user=request.user.id
    if user is None:
        return render(request, "alumnos.html")
    else:
        return render(request, "alumnos.html", {"url":avatares[0].imagen.url })

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
    avatares = Avatar.objects.filter(user=request.user.id)
    user=request.user.id
    if user is None:
        return render(request, "profesores.html")
    else:
        return render(request, "profesores.html", {"url":avatares[0].imagen.url })

@login_required
def ver_profesores(request):

    profesores = Profesores.objects.all()
    dicc =  {"profesores":profesores }
    plantilla = loader.get_template("ver_profesores.html")
    respuesta = plantilla.render(dicc)
    return HttpResponse(respuesta)

# -----------LOGIN---------- #
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            user = authenticate(username=usuario , password=contra)
            if user is not None:
                login(request , user )
                avatares = Avatar.objects.filter(user=request.user.id)
                return render( request , "inicio.html" , {"url":avatares[0].imagen.url, "mensaje":f"Bienvenido/a {usuario}"})
            else:
                return HttpResponse(f"Usuario no encontrado")
        else:
            return HttpResponse(f"FORM INCORRECTO {form}")

    form = AuthenticationForm()
    return render( request , "login.html" , {"form":form})

# -----------Registro---------- #

def register (request):

    if request.method == "POST":
        form = User_creation(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('Username')
            email = form.cleaned_data.get('Email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,email=email, password=raw_password)
            login(request,user)
            return redirect ('home')
    else:
        form = User_creation()
    return render(request,"registro.html",{"form":form})

# -----------Editar Perfil User---------- #

def editarPerfil(request):
    usuario= request.user
    if request.method=='POST':
        miFormulario = UserEditForm(request.POST, instance=usuario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.user =informacion["user"]
            password = informacion ["password1"]
            usuario.set_password(password)
            usuario.save()

            return render (request , "inicio.html")
    else:
        miFormulario = UserEditForm(initial ={'email': usuario.email})

    return render (request, "editar_perfil.html", {"miFormulario": miFormulario, "usuario":usuario} )



