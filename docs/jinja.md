## Jinja2

Es una libreria para generar documentos HTML de forma rápida y simple.

Al trabajar con Jinja2 hay que tener en cuenta 3 elementos importantes:
    * Variables {{ variable }}
    * Instrucciones {% instruccion %}
    * Comentarios {# comentario #}

### Uso de variables:

Podemos enviar objetos al template

~~~

<h2>Hola {{ username }} </h2>
<p>
    Te encuentras en el curso {{ course.title }}
</p>

~~~

### Uso de condicionales:

~~~

{% if user_is_admin %}
    <a href="{{ url_for('admin') }}">admin</a>
{% else %}
    <p>No cuentas con los permisos suficientes</p>
{% endif %}

{% if user_is_admin and user.permission_level == 5 %}
    <a href="{{ url_for('admin') }}">admin</a>
{% endif %}

~~~

### Uso de ciclos:
(Jinja2 solo permite el uso del ciclo **for**)

~~~
<ul>
    {% for val in [1,2,3,4,5,6,7,8,9] %}
        <li> {{ val }} </li>
    {% endfor %}
</ul>
~~~

Dentro del ciclo podemos acceder a diferentes atributos del objeto loop.

index: Interacción actual. El valor comienza en 1
index0: Iteración actual. El valor comienza en 0 (Ideal si deseamos replicar el comportamiento de la función enumerate)
first: Valor verdadero si nos encontramos en la primera iteración.
last: Valor verdadero si nos encontramos en la última iteración.
length: Número de iteraciones.
Ejemplo:

~~~

<ul>
    {% for val in [1,2,3,4,5,6,7,8,9] %}
        <li> {{ loop.index0 }} - {{ val }} </li>
    {% endfor %}
</ul>

~~~

### Funciones:

Se pueden enviar funciones propias al template a través de la función render template:

~~~

def suma(val1, val2):
    return val1 + val2

def suma_template():
     return render_template('suma.html', val1=10, 
                                         val2=30, funcion=suma)


<p>
La suma de {{ val1 }} + {{ val2 }} es : {{ funcion(val1, val2) }}
</p>
~~~