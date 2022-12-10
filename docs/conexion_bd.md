
Configurar el proyecto para que pueda conectarse a una base de datos.

Para poder conectarnos a la bd y manipularla, usaremos el ORM -> **peewee**

1) instalar el ORM -> **pip install peewee**

Para conectarnos con el gestor de bd (en este caso mySql) tenemos que instalar el cliente 

2) instalar el cliente -> **pip install mysqlclient**

Crear la bd:

3) autenticarnos con el servidor -> **mysql -u root** (usuario con el cual nos  vamos a autenticar)
(si no puedo autenticarme agregar el flag -p y colocar la contraseña -> mysql -u root -p)
   
4) una vez dentro del servidor, crear la bd -> **CREATE DATABASE nombre_de_la_bd;**
5) **use nombre_bd**
6) Ir al proyecto y crear un documento -> **database.py** donde haremos la conexión entre nuestro proyecto y la bd
7) importar el ORM -> **from peewee import * '**
8) definir una variable **database** -> 
   database = MySQLDatabase('nombre_proyecto', --- bd con la que nos vamos a conectar
                             user='usuario a autenticar', 
                             password='', 
                             host='localhost, 
                             port=3306) --- puerto x default de mysql

9) importamos la conexion en el archivo principal (main.py)              
10) para poder probar la conexion, usamos los eventos startup y shutdown
11) detener el servidor y cerrar el cliente mysql, volver a levantar
   

