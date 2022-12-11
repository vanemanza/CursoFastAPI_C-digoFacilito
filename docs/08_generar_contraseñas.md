Cuando creamos los usuarios, almacenamos la contraseña en texto plano, pero no es recomendable, por eso implementaremos un hash a la contraseña que nos envia el cliente, y para que posteriormente podamos autenticar a los usuarios.

Existen varios algoritmos de encriptación, pero en este ejemplo utilizaremos el hash MD5.(averiguar otros!)

1) para poder crear la contraseña, vamos a **definir** un método de clase en el modelo User (archivo database.py)
2) lo nombramos (create_password) y lo decoramos con @classmethod para que se considere un método de clase. Recibe dos parámetros, primero la clase y segundo, la contraseña en texto plano.
3) importamos el modulo hashlib
4) dentro de nuestro método de clase, creamos una variable **h**, que es una instancia de hashlib.md5()
5) h.update(password.encode('utf-8'))
6) retornamos h.hexdigest()

Luego vamos al archivo main.py y **usamos** el método recién creado, dentro de nuestra función **create_user**.

7) Modificamos el valor del parametro password, ya no vamos a almacenar texto plano, sino que vamos a almacenar el hash. -> hash_password = User(modelo) y llamamos al método de clase **create_password**, como argumento le pasamos lo que el cliente nos envia (user.password)
8) finalmente reemplazamos el texto plano (user.password) por el hash(hash_password)

