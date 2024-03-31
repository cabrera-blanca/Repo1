from django.urls import path
from . import views

#----- URL  Patterns -----

urlpatterns = [
    path('', views.inicio , name="home"),
    path('ver_cursos', views.ver_cursos , name="cursos"),
    path('alumnos', views.alumnos , name="alumnos"),
    path('alta_curso', views.curso_formulario),
    path('buscar_curso', views.buscar_curso),
    path('buscar', views.buscar),
    path('eliminar_curso/<int:id>', views.eliminar_curso ,name="eliminar_curso"),
    path('editar_curso/<int:id>', views.editar_curso, name='editar_curso'),
]
