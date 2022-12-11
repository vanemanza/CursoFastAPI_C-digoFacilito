Para validar datos de entrada y salida, debemos usar modelos, en vez de retornar un diccionario.

En schemas.py definimos un nuevo modelo:
    - UserResponseModel(BaseModel) que hereda de BaseModel
    - dentro colocamos los atributos que vamos a enviar al cliente.
  
Lo importamos en main.py y en vez de retornar el dict, retornamos un objeto de tipo UserResponseModel, con sus correspondientes valores como parámetros.

Ahora le indicamos a fastapi que vamos a serializar el objeto agregando en el decorador como segundo parametro que modelo vamos a utilizar como respuesta -> response_model=UserResponseModels

Usando modelos le indicamos que la respuesta de parte del servidor debe poseer ciertos atributos, que son requeridos, de que tipo son, y como respuesta se va a retornar un objeto serializado, o sea un json que se envia del servidor al cliente.
