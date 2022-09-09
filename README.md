# Ejemplo Deploy Hello World to Heroku

    basado en Deploy de Python en Heroku - Bytes por CódigoFacilito: https://youtu.be/t5G5YPEZWZ0

¿Te has preguntado como hacer el caso mas sencillo?

Tenemos:
1. Un *main.py* que al que se le han hecho algunas modificaciones.
2. Un archivo *requirements.txt* donde se guardan las dependencias a instalar
3. Un archivo *Proclife* asi tal cual, este archivo debe estar ubicado en el directorio raiz de tu aplicacion. No funcionara si se aplica en un subdirectorio. Basicamente colocamos que archivo se va a ejecutar en el servidor.

Una vez tengas lo anterior, necesitar ir a **HEROKU**. Y desde alli, vinculas el repositorio en GitHUb, le puedes indicar la rama. En este caso, le indique que la rama es: 

    deploy_heroku

Ahora bien, el proceso puede pareces sencillo, pero hasta que uno no lo hace por su cuenta, no aprende. 

Le habilite la funcionalidad *Automatic Deploys From* para que cada vez que actualize mi rama en Github, haga la correspondiente actualizacion.

*Puedes consultar la aplicacion aqui:*

**https://miappflask.herokuapp.com/**

## Usando Request Para Averiguar mi IP.

<img src="https://i.imgur.com/FbP6nZ8.jpg" width="100%"/>

Entender como FLASK usa las *Request* y *Responses* para poder regresar la infomracion solicitada. 

Se añadieron algunas lineas de codigo a main.py
