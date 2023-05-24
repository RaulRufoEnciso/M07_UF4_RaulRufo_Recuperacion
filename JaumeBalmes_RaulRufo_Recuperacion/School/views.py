from django.shortcuts import render, redirect
from .forms import *
# Create your views here.

def alumForm(request):
    form = AlumnosForm()
    context = {'form': form}
    return render(request, 'formularios/formAlumnos.html', context)
def profForm(request):
    form = ProfesorForm()
    context = {'form': form}
    return render(request, 'formularios/formProfesor.html', context)
