Hasta aquí, tenemos un servidor funcionando y ahora vamos a crear nuestro primer usuario, mediante una petición HTTP (metodo POST)

1) Crear una nueva ruta, desde el archivo **main.py**, crear una nueva función asincrona, **async def create_user()**, que se encargará de crear un nuevo usuario en la bd, y la decoramos con la función **@app.post('users/)**, los valores obligatorios que tiene que enviar el cliente para poder crear el usuario, son **username** y **password**. 
2) Para poder validar los valores de entrada y salida, fastAPI usa **pydantic**, ahora vamos a crear un nuevo archivo llamado **schemas** donde vamos a definir los modelos que nos permitan validar los datos de entrada y de salida.
3) importar de pydantic la clase **BaseModel**, esta clase nos permite validar que los valores almacenados para cada atributo de los modelos, corresponden al tipo de datos definidos en las anotaciones.
4) importamos las clase de BaseModel en el archivo main.py
5) los valores de entrada que envia el cliente, los definimos en los parametros de la funcion create_user(user:UserBaseModel).
6) dentro de la función, instanciamos un objeto de la clase User(de nuestro modelo de la bd) y ejecutamos el metodo create, que nos permite persistir un nuevo registro en la tabla.
7) definimos un valor para username y lo igualamos al valor user que nos envia el cliente por parametro, y accedemos a su atributo **username**
8) hacemos lo mismo con password
9) Asi creamos un nuevo usuario en nuestra bd, y definimos que el cliente obligatoriamente debe enviar valores para los atributos username y password, y ambos deben ser str.(en este ejemplo)
10) Para finalizar, retornamos al cliente el ID del objeto creado.