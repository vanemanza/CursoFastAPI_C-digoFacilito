Si necesitamos retornar un objeto de tipo Model (en este caso de Peewee), obtenemos un error de servidor, porque el valor no puede ser convertido en un diccionario, o sea que el objeto de tipo user, no puede ser serializado.

Para poder hacerlo, debemos enviar un diccionario y podemos hacerlo desde schemas.py definiendo una nueva clase.

Lo que hacemos es transformar cada atributo a llaves de un diccionario:
1) importar la clase GetterDict de Pydantic.utils
2) crear una clase, por ejemplo PeeweeGetterDict, que hereda de GetterDict, para poder obtener cada uno de los atributos del objeto
3) en la respuesta nuestro objeto de tipo Model se va a convertir a un objeto de tipo UserResponseModel, mas especificamente convertiremos cada atributo en llaves de un diccionario, de esta forma solo enviaremos al cliente los atributos definidos dentro de Schemas.
4) en nuestra nueva clase PeeweeGetterDict sobreescribimos el metodo get, que recibe 3 parametros, self, key y default, siendo estos de tipo Any, clase que debemos importar desde typing
5) dentro del metodo vamos a intentar obtener cada atributo del objeto model y compararlos con los atributos del modelo userResponsemodel, de forma de obtener solo los que coincidan en ambos modelos ( sean instancias de)
6) Tambien debemos importar la clase ModelSelect desde Peewee para poder verificar si la respuesta es instancia del modelo de peewee.

7) ahora dentro de la clase UserResponseModel de schemas, creamos una clase Config, con los atributos orm_mode y getter_dict a quien le asignaremos nuestra nueva clase (PeeweeGetterDict)
