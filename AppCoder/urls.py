from django.urls import path
from . import views

#----- URL  Patterns -----

urlpatterns = [
    path('', views.inicio , name="home"),
    #---Alumnos---#
    path('alumnos', views.alumnos , name="alumnos"),
    path('ver_alumnos', views.ver_alumnos , name="ver_alumnos"),
    path('alta_alumnos', views.alumno_formulario),
    path('buscar_alumnos', views.buscar_alumno),
    path('buscar_dni', views.resultado_alumno),
    path('eliminar_alumnos/<int:id>', views.eliminar_alumno ,name="eliminar_alumnos"),
    path('editar_alumnos/<int:id>', views.editar_alumno, name='editar_alumnos'),
    #---Cursos---#
    path('ver_cursos', views.ver_cursos , name="cursos"),
    path('alta_curso', views.curso_formulario),
    path('buscar_curso', views.buscar_curso),
    path('buscar', views.buscar),
    path('eliminar_curso/<int:id>', views.eliminar_curso ,name="eliminar_curso"),
    path('editar_curso/<int:id>', views.editar_curso, name='editar_curso'),
    #---Profesores---#
    path('profesores', views.profesores , name="profesores"),
    path('ver_profesores', views.ver_profesores, name="ver_profesores"),
]
