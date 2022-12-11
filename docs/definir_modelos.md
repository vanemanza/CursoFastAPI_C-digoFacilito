Para definir los modelos de la bd, o sea las tablas, en el archivo database.py definimos cada clase y hacemos que hereden  de la clase Model del FastAPI.
Luego definimos los atributos (columnas de la tabla) para cada modelo, sobre escribimos  el método str y la clase Meta.
Paso seguido, creamos las tablas, para ello en el archivo main.py importamos los modelos creados. Luego en la funcion startapp, agregamos el método connections.create_tables() que se encargará de crear la tabla en la bd, esté método  recibe como argumentos los modelos que deseamos crear.(si las tablas existen, no realiza cambios y sino las crea)
Para probar que todo funcione, bajo y levanto nuevamente el servidor, si no tengo errores, las tablas deberian haberse creado de  forma exitosa.

Ahora podemos ingresar a la bd y verificar si existen las tablas y agregar datos a las mismas:
1) mysql -u root -p
2) use fastapi_project;
3) show tables;
4) DESC users; etc para ver el detalle de cada tabla

