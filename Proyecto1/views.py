from django.http import HttpResponse
import datetime as dt
from django.template import Template,Context,loader
import random

def bienvenida(request):
    return HttpResponse("Buenasssss")

def hora_actual(request):
    ahora= dt.datetime.now()
    return HttpResponse("1La hora es {ahora.hour}")

def saludar(request,nombre):
    return HttpResponse(f"te estoy saludando {nombre}")

def inicio(request):
   # f=open(r"C:\Users\alejo\OneDrive - Alumnos Facultad de Ingeniería - UNLP\Python\Proyecto\Proyecto1\Proyecto1\templates\inicio.html")

    #plantilla= Template(f.read())

    #f.close

    aleatorio=random.randint(1,100)
    
    info={"numero":aleatorio}

    #contexto= Context(info)

   
    plantilla=loader.get_template("inicio.html")
    return HttpResponse(plantilla.render(info))