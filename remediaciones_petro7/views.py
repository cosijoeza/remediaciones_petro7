from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
import pyodbc

#primer vista prueba
def test(request):
    temas = ["Plantillas","Modelos","Vista"]
    #temas = []
    #Plantilla
    doc_externo = open("/home/cosi/Documentos/proyectosDjango/remediaciones_petro7/remediaciones_petro7/plantillas/test.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    #Contexto
    ctx = Context({"temas": temas})
    #Render
    documento = plt.render(ctx)
    return HttpResponse(documento)

#Segunda vista
def index(request):
    direccion_servidor = '10.0.7.89'   #Nombre del servidor
    nombre_bd = 'arcadia_cbos'         # Nombre de la base de datos
    nombre_usuario = 'Arcadia_DBPROD'   # Usuario de la BD
    password = 'Arcadia.P7'             #Conraseña de la BD
    resultados = []
    try:
        conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + 
                                direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)  
        cur = conexion.cursor()
        resultados.append("CONEXION EXITOSA!!")
        #print("CONEXION EXITOSA!!")

        resultados.append("select top 5 * from merchandiseeventline where id in (106777388,107545554)")
        # Se hacen las consultas, recuerden las secuencias de escape para las consultas
        cur.execute('select top 5 * from merchandiseeventline where id in (106777388,107545554)')
        
        #Devuelve una de las filas de resultados y en sucesivas llamadas nos irá devolviendo el resto
        consultas = cur.fetchall()
        
        for consulta in consultas:
            resultados.append(consulta.id)
        #   print(consulta.id)

    except Exception as e:
        resultados.append("Ocurrió un error al conectar a SQL Server: ",e)
        #print("Ocurrió un error al conectar a SQL Server: ", e)

    #Plantilla
    doc_externo = loader.get_template('index.html')
    #Diccionario
    ctx = {"resultados": resultados}
    #Render
    documento = doc_externo.render(ctx)
    return HttpResponse(documento)
