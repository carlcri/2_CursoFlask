*Puedes consultar la aplicacion aqui:*

**https://miappflask.herokuapp.com/**

**Flask Bootstrap**
Las extensiones o librerias o paquetria que nos permite agregar funcionalidad a Flask. Ya hemos visto algunas herramientas que nos provee Flask, como son:

- app.errorhandler
- url_for

**¿Que es un Framework?**
Es un conjunto estandarizado de conceptos, prácticas y criterios para enfocar un tipo de problemática particular que sirve como referencia, para enfrentar y resolver nuevos problemas de índole similar.

Vamos a incrementar funcionalidades en Flask con Bootstrap que nos va permitir crear una interfaz de usuario un poco mas agradable. 

Bootstrap es un "framework frontend" que tiene archivos htmal, css y JavaSript(JS). Bootstrap fue creado por Twitter, para generar interfazes de usuario.

**Instalacion Bootstrap**
Ve al archivo de requirements y anade: flask-bootstrap, e instalalo con pip, dentro del entorno virtual.

    pip install -r requirement.txt

**Inicializacion**
Se crea una instancia de Bootstrap y se le pasa como parametro una aplicacion de Flask    

    bootstrap = Bootstrap(app=app)

A partir de este momento, ya podemos tener acceso a los archivos CSS, HTML y JS de Bootstrap

**Primera Implementacion**

En el archivo base.html implementamos bootstrap, esto significa que substancialmente lo vamos a cambiar. Bootstrap ya tiene por defecto muchas funcionalidades implementadas. Bootstrap tambien tiene internamente un  *base.html*

POr ejemplo, en lugar de un *head* vamos a tener un *block head*, en lugar de un *body* tendremos un *block body*

<img src="https://i.imgur.com/oPuv1l9.jpg" width="70%"/>

Luego de modificar el *base.html* observamos un antes y despues en nuestra interfax de usuario:

#### Antes
<img src="https://i.imgur.com/1pH3SpV.jpg" width="40%"/>

#### Despues
<img src="https://i.imgur.com/29NFlqH.jpg" width="40%"/>


**Segunda Implementacion**

Podemos ir a la documentacion de Bootstrap e ir a la parte de *navbar* y buscar la que mas se adecue al proyecto. Para este caso, implementaremos una que dejo el instructor, y la modificaremos en *navbar.html*

El icono de Platzi, ira a la ruta *index*

Veras una *navbar* que mejora substancialemtne la experiencia de usuario.

**Mas Informacion**

https://pythonhosted.org/Flask-Bootstrap/

https://getbootstrap.com/docs/3.3/

*Para actualizarse a Bootstrap 4 y 5*

https://github.com/helloflask/bootstrap-flask/fork


## Configuración de Flask

Para activar el development mode debes escribir lo siguiente en la consola de WSL:

    export FLASK_ENV=development
    echo FLASK_ENV

Realmente no vi la diferencia. Hay que revisar el tema.

**Objeto Session**

Ya utilizamos el objeto *request* para obtener la direccion IP del usuario, y guardarla en una *Cookie* en el Web Browser

    user_ip = request.cookies.get('user_ip')

Esto no es una buena practica de seguridad porque cualquiera podria copiarla o modificarla a su antojo(tu mismo lo puedes hacer en este momento y cambiar la IP por cualquier cosa)

<img src="https://i.imgur.com/QkgC3AH.png" width="140%"/>

### ¿Como solucionarlo?

Hay otro objeto de Flask llamada *session* que se usa para guardar informacion del usuario de manera segura, y a continuacion mostrare porque.

Entonces vamos a crear una llave secreta: Una propiedad del objeto app() que es recordemos es de la clase Flask

Ahora en vez de guardar directamente la ip del usuario en una cookie, la vamos a guardar en una seccion. 

1. Hay un atributo del objeto FLASK llamado *config*, recomiendo esta lectura. Y funciona como un diccionario. Lo usaremos para generar una llave secreta

    app.config['SECRET_KEY'] = 'misecreto'

2. Importamos el objeto *session*, y posteriormente guardamos la *user_ip* en el objeto. Finalmente, en la ruta *welcome* y con el metodo *get* lo consultamos y guardamos:


        from flask import session
        ...
        ...
        session['user_ip'] = user_ip
        ...
        ...
        user_ip = session.get('user_ip')


Se corre nuevamente la aplicacion, y encontramos que la informacion esta encriptada.

<img src="https://i.imgur.com/dmXfgCa.png" width="100%"/>

### Ademas se session y request, Flask tambien tiene otros dos objetos de interes:

- session: storage que permanece entre cada request
- request: informacion sobre la peticion que realiza el browser
- current_app: la aplicacion actual
- g: storage temporal, se reinicia en cada request - tambien es un diccionario


Lecturas recomendada: 

- https://flask.palletsprojects.com/en/1.1.x/config/ 
- https://prettyprinted.com/tutorials/automatically_load_environment_variables_in_flask

