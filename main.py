from wsgiref.simple_server import make_server

def application(env, start_response):
    headers = [('Content-type', 'text/plain'),]

    start_response('200 OK', headers)

    return ['Hola mundo desde mi primer server con python'.encode('utf-8')]

server = make_server('localhost', 8001, application)

server.serve_forever()