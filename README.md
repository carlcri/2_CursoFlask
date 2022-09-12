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

## Templates con Jinja 2

Un template es un archivo .html que permite renderiar informacion estatica y dinamica, para este caso podriamos pasar la informacion de la ip del usuario directamente al html, en lugar de regresarla como una cadena de texto.

Vamos a crear un nuevo directorio llamado templates, e importa de la clase Flask el modulo render_template

en la ruta hello, donde ahora en vez de retornar una cadena, retornamos el template: hello.html

tambien enviamos la user_ip, y dentro del html, coloccamos doble corchete, para indicar es una variable

Asi se veria en el servidor local:

<img src="https://i.imgur.com/KO2Xk1E.jpg" width="100"/>

Lectura recomendada: https://jinja.palletsprojects.com/en/3.1.x/


## Estructuras de control

La idea es crear una lista de frutas en la *aplicacion*, ya sabemos que la aplicacion es *main.py*, y que la mostraremos en la ruta *welcome*, siempre y cuando se cumpla la condicion. *¿Cual es esa condicion?* Lo explicare mas adelante.

**¿Que es el contexto de la aplicacion?** Es un concepto en construcion, sin embargo cuando una aplicacion maneja muchas variables, es mejor crear un diccionario con los parametros que vamos a pasar, y posteriormente expandir el diccionario, con la notacion **context

    @app.route('/hello')
    def hello():
        user_ip = request.cookies.get('user_ip')
        context ={
            'user_ip':user_ip,
            'fruits':fruits,
    }
    return render_template('hello.html', **context )



**En el template welcome**

Se guarda la IP del Usuario en una Cookie en la ruta raiz, como se ha venido haciendo, y nos redirige a la ruta *welcome*. 

De encontrarse la *user_ip* la mostrara, seguido de la lista de frutas, aconcejo hacerlo con el tag *ul*. 

¿Que es el *HTML tag* *ul*? An unordered HTML list. Es para que el Browser entienda que es una lista, y la usaremos para desplegar nuestra lista de frutas, si se cumple la condicion. 

De NO encontrarse la IP del usuario, desplegara un mensaje y un enlace hacia la raiz para intentar obtenerla.

La haremos en el html:

Para todos los templates, Flask pone a nuestra disposicion una variable que se llama url_for que nos permite encontrar la ruta especifica, con enviar el nombre de la funcion que pertenece a esta ruta.

        {% if user_ip %}
        <h3>Your IP is {{user_ip}}</h3>
        <ul>
            {% for fruit in fruits %}
                <li>{{fruit}}</li>
            {% endfor %}
        </ul>
        {% else %}
            <a href="{{url_for('index')}}">Ir a inicio</a>
            <h3>Cookie Not Found</h3>
        {% endif %}

Como vez index es la funcion que pertenece a la ruta raiz, y la que guarda la ip del usuario.


## Hago una busqueda y mostrarla en una ruta

Se realiza una busqueda estatica en *DataWorkers.py*, y se renderiza en la ruta *welcome*. Mira que se usa para la busqueda, funciones de orden superior-*high orfer functions*

Cada vez que se refresque la pagina, mostrara una busqueda diferente.

## Herencia de Templates: como incluir templates en otros templates

 Muy util porque permite heredar y reutilizar codigo *html*. Lo primero es crear un archivo base.html el cual vamos a extender en todos nuestros templates. El base.html hay quue guardarlo en el folder *templates*, si Visual Studio Genera uno por defecto, guardarlo asi.

 1. El template *welcome.html* se deja con lo mas basico

        {% extends 'base.html'%}: 
        
Sintaxis en Jinja para indicar que el template hereda o es hijo de base.html 👆

Si colocacomos solo esta linea de codigo, y corremos el servidor, pues no nos va a mostrar nada. Porque FLAKS esta rendereando base.html, y cuando el buscador ve que termina el HTML, no rendera nada mas. 

Entonces se haran modificaciones tanto en los templates de *consultas y welcome*, usando una estructura de bloques 

Vamos tambien a familiarizarnos dicha estructura: en este caso un bloque de titulo, para la ventana que se genera, esto para el base.html. El simbolo *pipe* al lado de Coronapp es solo un separador. 

    {% block title%}
        Coronapp|
    {% endblock%}

Y este para el welcome.html

    {% block title%}
        welcome 
    {% endblock%}

En este caso si corremos el servidor Flask tal y como lo hemos venido haciendo, el bloque titulo en hello.html esta sobrescribiendo, pero nosostros lo que queremos es juntarlo. Necesitamos anadir, entre otras cosas, este statement, dentro del bloque. 

    (super de superclase): {{super()}}

Asi:

    {% block title%}
        {{super()}}
        Consultas
    {% endblock%}

