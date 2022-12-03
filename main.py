from jinja2 import Environment, FileSystemLoader


from wsgiref.simple_server import make_server

# levantar un servidor con wsgi que retorne  texto plano
# def application(env, start_response):
#     headers = [('Content-type', 'text/plain'),]

#     start_response('200 OK', headers)

#     return ['Hola mundo desde mi primer server con python'.encode('utf-8')]

# server = make_server('localhost', 8001, application)

# server.serve_forever()

def application(env, start_response):
    headers = [('Content-type', 'text/html'),] # cambio texto plano por html

    start_response('200 OK', headers)

    env = Environment(loader=FileSystemLoader('templates')) #ruta donde se encuentran los templates

    template = env.get_template('index.html') # obtener el template 

    # lo renderizamos y almacenamos en una variable para retornar al cliente.
    html = template.render(
        {
            'title': 'Servidor en Python',
            'name': 'Vane'
        }
    ) 
    # acá los valores estan hardcodeados pero podemos obtenerlos de una bd generando una conexion con la misma
    # o consumirlos desde una API o leer un archivo

    return [bytes(html, 'utf-8')]

server = make_server('localhost', 8000, application)

server.serve_forever()