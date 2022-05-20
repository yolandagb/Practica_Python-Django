from re import template
from time import time
from django.http import HttpResponse

def saludo (request):
    return HttpResponse("Hi, Im leraning Django")

def secondview (request):
    return HttpResponse ("Creo que he entendido como funcioan django")
    
import datetime

def today(request):
    day = datetime.datetime.now()
    textDocument = f"Hoy es  día </br> {day}"
    return HttpResponse(textDocument)

def myName(self, name):
    textDocument1 = f"My name is </br> {name}"
    return HttpResponse(textDocument1)

from django.template import Template, Context
from django.template import loader

def probandoTemplate(self):

    miHtml = open("\Users\ygarcia\Desktop\django\web_project\templates\index.html")

    template = Template(miHtml.read()) #Se carga en memoria nuestro documento, template1   
    ##OJO importar template y contex, con: from django.template import Template, Context

    miHtml.close() #Cerramos el archivo

    miContexto = Context() #EN este caso no hay nada ya que no hay parametros, IGUAL hay que crearlo

    documento = template.render(miContexto) #Aca renderizamos la plantilla en documento

    return HttpResponse(documento)


