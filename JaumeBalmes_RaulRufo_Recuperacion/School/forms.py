from django.forms import ModelForm
from .models import Alumnos, Profesor

#Formulario para los alumnos
class AlumnosForm(ModelForm):
    class Meta:
        model = Alumnos
        fields = '__all__'

#Formulario para los profesores
class ProfesorForm(ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'