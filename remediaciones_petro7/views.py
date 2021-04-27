from django.http import HttpResponse
import datetime as dt
#primer vista
def hola(request,edad):
    #edad = edad - 10
    fecha_actual = dt.datetime.now()
    return HttpResponse("%s---%s ¡Hola mundo :)!" %(edad,fecha_actual)) 
