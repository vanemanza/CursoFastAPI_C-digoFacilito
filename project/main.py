from fastapi import FastAPI

app = FastAPI(title='Proyecto para reseñar peliculas', description='En este proyecto seremos capaces de reseñar peliculas', version=1)

# para levantar el servidor ejecutamos en la terminal el comando -> uvicorn main:app --reload (para q reinice automaticamente)

# con el decorador app.get registro una nueva ruta
@app.get('/')
async def index(): 
    return "Vamo' Argentina carajo!!!!"

# async indica q la función se va a ejecutar de  forma asincrona, o sea q si se realizan muchas peticiones al mismo tiempo sobre la misma url, 
# podrán ser resueltas de forma asincrona.

@app.get('/about')
async def about():
    return "About"

# Resumen para poder registrar urls con fastapi, definimos una funcion asincrona, y la decoramos con la aplicacion, dependiendo del metodo, 
# sera el metodo de la app q implementaremos, y el argumento es la ruta que queremos registrar.