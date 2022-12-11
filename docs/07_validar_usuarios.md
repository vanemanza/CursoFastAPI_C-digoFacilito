Para poder implementar reglas de negocio, por ejemplo poner una condición sobre la longitud del nombre de usuario para poder crearlo, podemos hacerlo validando dicha longitud.

Para implementar validaciones con fastapi, nos apoyamos en la clase BaseModel, usando pydantic y metodos de clase.

1) En nuestra clase UserBaseModel, vamos a implementar un método de clase llamado username_validator, que recibe como primer parámetro la clase y como segundo el valor que le daremos al atributo, en este caso username.
2) para que el método sea considerado una validación debe ser decorado con @validator y recibe como argumento el nombre del atributo que queremos validar.(importar validator desde pydantic)
3) dentro del método colocamos nuestras reglas, por ejemplo cual debe ser la longitud del username.
4) para confirmar que la validación fué exitosa, retornamos el valor.

En síntesis, para que la funcion create_user pueda ejecutarse, debe recibir un objeto del tipo UserBaseModel, el cual debe poseer los atributos descriptos en schema.py y cumplir con todas las validaciones.

