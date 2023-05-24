from django.urls import path
from . import views

#Rutas de School
urlpatterns = [
    path('form/Alumno/', views.alumForm, name='Alumnos_Form'),
    path('form/Profesor/', views.profForm, name='Profesor_Form'),

]