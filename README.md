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

<img src="https://i.imgur.com/FbP6nZ8.jpg" width="50%"/>

Entender como FLASK usa las *Request* y *Responses* para poder regresar la infomracion solicitada. 

Se añadieron algunas lineas de codigo a main.py

## Basico ciclo request and response, dos rutas

Se crea una nueva ruta llamada *Welcome*, adicional a la ruta raiz.

En la ruta raiz se van a colocar estos staments que indican, el primero redirecionandome a la ruta *welcome*, y la segunda, que coloque una *cookie* en nuestro navegador que va a ser igual a la ip del usuario.  

    response = make_response(redirect('/welcome'))
    response.set_cookie('user_ip', user_ip)

En la ruta *welcome*, el siguiente, indica obtendra la ip del usuario no directamente del request, como estaba anteriormente, sino de las *cookie*

    user_ip = request.cookies.get('user_ip')

Para visualizar las cookies en EDGE hay que ir a herramientas de desarrollador dentro del *browser*

<img src="https://i.imgur.com/1J0WMvg.jpg" width="40%"/>

Y dento de estra cruzecita buscar *Aplicacion*, y luego *Almacenamiento*
