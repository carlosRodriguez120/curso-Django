
from django.http import HttpResponse
import datetime

from django.shortcuts import render

class persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


def saludo(request):
    persona1 = persona("jose ", "Rodriguez")
    temas = ["plantillas", "modelos", "formularios", "vistas", "despliegue"]
    ahora = datetime.datetime.now()
    contexto = {"nombre_Persona": persona1.nombre, "apellido_Persona": persona1.apellido, "momento_Actual": ahora,
                        "temas": temas}  # puede recibir parametros como diccionarios
    return render(request,"miPlantilla.html",contexto)































def despedida(request):
    return HttpResponse("adios")


def hora(request):
    fechaActual = datetime.datetime.now()
    documento = """
    <html> 
    <body>
    <h1>
    fecha y hora actual es: %s
    </h1>
    </body>
    </html>
    """ % fechaActual
    return HttpResponse(documento)


def calcularEdad(request, edad, anio):
    peirodo = anio-2022
    edadFutura = edad+peirodo
    documento = "<html><body><h2>en el año %s tendras %s años </h2></body></html>" % (
        anio, edadFutura)
    return HttpResponse(documento)
