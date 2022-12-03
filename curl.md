### curl:

**command line tool and library for transferring data with URLs**

C ( client ) + URL

Para realizar las peticiones podemos hacerlo con [httpbin.org](http://httpbin.org/)

Para verificar si curl está instalado -> **curl --version**

1) realizar una petición **get**: 
    **curl https://httpbin.org/get**
    obtengo un json con los siguientes atributos:   - args(argumentos)
                                                    - headers(encabezados)
                                                    - origin
                                                    - url

2) enviar valores por **parámetros**: 
    **curl "https://httpbin.org/get?name=Vanesa&lastname=Manza"**
    el parámetro ingresado se verá dentro del atributo args

3) enviar valores en el **encabezado** de la petición:
    **curl "https://httpbin.org/get?name=Vanesa&lastname=Manza" -H "accept: application/json"**
    con el flag **-H**, en este caso le indico al servidor que el cliente puede aceptar un objeto json como respuesta.
    el valor enviado se verá dentro del atributo headers.
    Para enviar muchos encabezados, se usa un -H por cada encabezado que queremos enviar.

4) si del lado del cliente, queremos conocer todos los encabezados que se envian como parte de la respuesta usamos la bandera **-i**    
     **curl "https://httpbin.org/get?name=Vanesa&lastname=Manza" -H "accept: application/json" -i**
     En este caso la petición se divide en dos partes:
        - Arriba los encabezados de la respuesta (fecha, content-type, content-length, server, etc)
        - Abajo el cuerpo de la respuesta (el objeto json)

5) Modificar el **metodo de la petición** con la bandera **-X** y luego el método en Mayúsculas.
    Por default se hace GET
      **curl -X GET "https://httpbin.org/get?name=Vanesa&lastname=Manza" -H "accept: application/json" -i**

6) Consumir el endpoint **/post** 
    **curl -X POST https://httpbin.org/post**
    Obtengo como respuesta por parte del servidor un json.
    El objeto tiene diferentes atributos (argumentos, data, archivos, formulario, encabezados, un objeto json, el origen y la url)
    Para enviar valores en el cuerpo de la petición, usamos la bandera **-d** y entre comillas simples construimos el json.
    **curl -X POST https://httpbin.org/post -d '{"username":"Vane", "password":"123"}'**
    En el atributo form encontraremos nuestro objeto.

7) Consumir el endpoint **/put**
   **curl -X PUT https://httpbin.org/put**
   El orden de las banderas no es relevante, puedo colocar una **-H** antes de la **-X**
   **curl -H "accept: application/json" -X PUT https://httpbin.org/put**
   **curl -H "accept: application/json" -X PUT -d '{"username":"Vane"}' https://httpbin.org/put -i**

__**Resumen**__:
* **-H** para enviar valores en el encabezado
* **-X** para indicar el método (verbo)
* **-d** para enviar valores en el cuerpo de la petición
* **-i** para visualizar el encabezado de la respuesta
















