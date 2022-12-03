### WSGI

**Web Server Gateway Interface**

Es un estándar para escribir programas que puedan comunicarse a traves del protocolo HTTP,
dicho programa podrá ejecutarse en un servidor web tal como Apache o nginix.
Está  inspirado en el estándar Common Gateway Interface o CGI.

~~~ 
from wsgiref.simple_server import make_server

def application(environ, start_response):
    headers = [('Content-type', 'text/plain; charset=utf-8')]

    start_response('200 OK', headers)

    return ['Hola gente de códigofacilito'.encode('utf-8')]

server = make_server('localhost', 8000, application)
server.serve_forever()
~~~

Al importar la función **make_server**, podremos generar nuestro servidor.

La función recibe tres argumentos obligatorios:
    - La dirección del servidor,
    - el puerto y 
    - la _función handler. La función como observamos posee dos parámetros:
                                                                      -  environ 
                                                                      -  start_response.

    El parametro env es un diccionarion el cual contiene variables wsgi relacionadas con la petición del cliente (Método del protocolo, Query String etc ...)

    El parametro start_response es un callback el cual recibe, de forma obligatoria, dos argumentos. El estatus y los encabezados de la respuesta.

Dentro de la función definimos los encabezados de la respuesta, de igual forma indicamos el status code, en este caso 200, finalmente retornamos un recurso.    

**En lugar de texto plano, podemos retornar un HTML:**

~~~
from wsgiref.simple_server import make_server

HTML = """
<!DOCTYPE html>
<html>
  <head>
    <title>Título</title>
  </head>
  <body>
    <h1>Hola gente de códigofacilito</h1>
  </body>
</html>
"""

def application(environ, start_response):
    headers = [ ('Content-type', 'text/html; charset=utf-8') ]

    start_response('200 OK', headers)

    return [bytes(HTML, 'utf-8')]

server = make_server('localhost', 8000, application)
server.serve_forever()
~~~




