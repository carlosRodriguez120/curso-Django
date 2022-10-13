from django.template import Template, Context
from django.http import HttpResponse
import datetime


class persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


def saludo(request):
    persona1 = persona("carlos ", "Rodriguez")
    temas = ["plantillas", "modelos", "formularios", "vistas", "despliegue"]
    ahora = datetime.datetime.now()
    doc_Externo = open(
        "C:/Users/USER/Desktop/ProjectDjango/Proyecto1/Proyecto1/Plantillas/miPlantilla.html")
    plantilla = Template(doc_Externo.read())
    doc_Externo.close()

    contexto = Context({"nombre_Persona": persona1.nombre, "apellido_Persona": persona1.apellido, "momento_Actual": ahora,
                        "temas": temas})  # puede recibir parametros como diccionarios
    documento = plantilla.render(contexto)
    return HttpResponse(documento)


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
