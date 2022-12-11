from fastapi import FastAPI
from database import database as connection # importo la conexión a la bd
from database import User, Movie, UserReview 

from schemas import UserBaseModel

app = FastAPI(title='Proyecto para reseñar peliculas', description='En este proyecto seremos capaces de reseñar peliculas', version=1)
# para levantar el servidor ejecutamos en la terminal el comando -> uvicorn main:app --reload (para q reinice automaticamente)

@app.on_event('startup')
def startup():
    print ('La magia va a comenzar, arriba esos servidores 👾 !!!')
    if connection.is_closed():
        connection.connect
        print(f'Connected - ready !')
    connection.create_tables([User, Movie, UserReview])    


@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        print(f'connection is close ') # no imprime!
        connection.close
    print ('El servidor va a finalizar. Hasta la vista Servi 😎 !!!')    

# con el decorador app.get registro una nueva ruta
@app.get('/')
async def index(): 
    return "Vamo' Argentina carajo!!!!"

# async indica q la función se va a ejecutar de  forma asincrona, o sea q si se realizan muchas peticiones al mismo tiempo sobre la misma url, 
# podrán ser resueltas de forma asincrona.

# @app.get('/about')
# async def about():
#     return "About"

# Resumen para poder registrar urls con fastapi, definimos una funcion asincrona, y la decoramos con la aplicacion, dependiendo del metodo, 
# sera el metodo de la app q implementaremos, y el argumento es la ruta que queremos registrar.

@app.post('/users')
async def create_user(user: UserBaseModel):
    
    user = User.create(
        username=user.username,
        password =user.password
    )
    return user.id 