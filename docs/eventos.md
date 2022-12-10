Los eventos en fastapi, sirven para programar acciones que queremos que se ejecuten antes o despues de que ciertos acontecimientos ocurran.

Por ejemplo, con  **startup** y **shutdown** podemos programar eventos que queremos que se ejecuten cuando el servidor inicie o esté finalizando. 
Para ello definimos dos funciones, la primera **def startup()** se ejecutará cuando el servidor esté por comenzar, y la segunda función **def shutdown()** que se ejecutará cuando el servidor esté finalizando.Para poder programarlas hay que decorarlas utilizando la app seguida del método on_event -> **@app.on_event('startup')** y recibe como argumento el nombre del evento que va a disparar la función (startup)

Para probar, desde la terminal, frenar el servidor si está corriendo y volverlo a levantar -> **uvicorn main:app --reload**

(- **TODO** buscar otros eventos en la documentación oficial de fastapi)