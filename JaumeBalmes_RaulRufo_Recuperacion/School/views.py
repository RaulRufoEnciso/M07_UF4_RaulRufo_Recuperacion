from django.shortcuts import render, redirect
from .forms import *
# Create your views here.

def alumForm(request):
    form = AlumnosForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('index_alum')
    context = {'form': form}
    return render(request, 'formularios/formAlumnos.html', context)
def profForm(request):
    form = ProfesorForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('index_prof')
    context = {'form': form}
    return render(request, 'formularios/formProfesor.html', context)

def alums(request):
    alumnos = Alumnos.objects.all()
    context = {'alumno':alumnos}
    return  render(request, 'crud/Alums.html', context)
def profs(request):
    profesores = Profesor.objects.all()
    context = {'profs':profesores}
    return  render(request, 'crud/Profs.html', context)
