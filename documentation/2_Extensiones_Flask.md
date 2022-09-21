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

## Implementacion de Flask-Bootstrap y Flask-WTF

Si queremos que el usuario pueda enviar informacion a nuestra aplicacion WEB, esto se hace mediante una forma. *Flask-WTF* es una extension que ayuda a integrar WTF en Flask. Dentro del requirements.txt, anadir una entrada:

    flask-wtf

Despues de instalarlo, lo importamos al *main.py*:

    from flask_wtf import FlaskForm

Tambien necesitamos los fields:

    from wtforms.fields import PasswordField, StringField

**RETO1**

Crear una forma para que enviar el usuario y la contraseña en una nueva ruta que se llamara *login*. Se necesita un boton de *enviar*

1. Declaramos una clase que usaremos mas adelante que extiende o hereda de FlaskForm, con dos campos, que por ahora no lo vamos a usar pero enventualmente los vamos a necesitar, lo que esta entre parentesis se conoce como etiqueta.

        class LoginForm(FlaskForm):
            username = StringField('Nombre de Usuario')
            password = PasswordField('contraseña')
            submit = SubmitField('Enviar')

2. Creamos la ruta en el main, y enviamos en el contexto el loginform

        @app.route('/acceso')
        def login():
            # se instancia un objeto de clase LoginForm
            loginform = LoginForm()
            context = {'loginform':loginform}

            return render_template('acceso.html', **context)

3. La forma mas sencilla para renderizar la forma es usar Bootstrap en *acceso.html*, asi que lo importamos, y lo incluimos en el bloque de contenido:

        {% import 'bootstrap/wtf.html' as wtf%}
        ...
        ...
        {{wtf.quick_form(loginform)}}

### Y este es el resultado:

<img src="https://i.imgur.com/87h2nKu.jpg" width="65%"/>

**Reto2**

Mejorar la version anterior para que valide y no se envie la forma vacia, y un poco el aspecto de la *forma*.
Tambien se necesita colocar la clase LoginForm en un nuevo archivo.

1. Para que no se envie la forma vacia, se necesita usar un validador que se llama *DataRequired*

        from wtforms.validators import DataRequired

2. Integrar los validadores a la clase. *validators* recibe como parametro una lista de validadores, es importante que se pase una nueva instancia del validador por eso *DataRequired()* tiene esos parentesis.

        class LoginForm(FlaskForm):
            username = StringField('Nombre de Usuario', validators=[DataRequired()])
            password = PasswordField('contraseña', validators=[DataRequired()])
            submit = SubmitField('Enviar')


3. Dentro de un tag *div* que va a ser de clase *container*, dicha clase viene de Bootstrap.

### Y este es el resultado:

<img src="https://i.imgur.com/Ysgxj8q.jpg" width="65%"/>

Ahora ya no se podra enviar la forma vacia, y queda dentro de un container

4. En la siguiente seccion, vamos a mover la clase donde tiene que estar, y desde ahi la vamos a importar.

## App Factory

Tal como lo prometi, vamos a mover la *clase* y nos adelantaremos un poco a la seccion de *App factory*

**¿Que es App Factory? **
Es simplemente una funcion que regresa la nueva app. Y para ello se cambiara substancialmente la estructura de la aplicacion.

Los cuadros azules representan carpetas y las figuras amarillas son los archivos

<img src="https://i.imgur.com/J0Cy9gj.png" width="100%"/>

1. Se crea un nuevo directorio en la raiz llamado *app*, y dentro un archivo llamado 

        __init__.py

Y dentro definiremos la funcion *create_app*

        def create_app():
            app = Flask(__name__)
            bootstrap = Bootstrap(app=app)

            # Se hace uso del atributo config de FLASK para generar una llave secreta
            app.config['SECRET_KEY'] = 'misecreto'

            return app

2. Llamar a la funcion en *main.py*, y crear una instancia de la aplicacion, o para que me entienda crearla.

        from app.auth import create_app
        ...
        ...
        app = create_app()

3. Mover los directorios *static* y *templates* al directorio *app* que es donde la app los va a buscar.         

4. Probamos la aplicacion, y perfecto, ¡Felicitaciones! Faltan algunas tareas

5. Mover la forma a un nuevo archivo llamado *forms.py* e importarla en el *main*

        from app.forms import LoginForm


Probamos la aplicacion, y el funciona como lo venia haciendo. 

En la siguiente implementacion, haremos uso del archivo *config.py* para guardar la llave secreta.

## APP Factory Parte 2

Creamos una clase en el archivo *config.py* para guardar la llave secreta. Donde SECRET_KEY es un aributo de la misma.

        class Config:
            SECRET_KEY = 'misecreto'

MOdificamos el archivo **__init__.py**; importamos la clase; y modificamos el atributo *config* del objeto FLASK

        from .config import Config
        ...
        ...
        app.config.from_object(Config)

**Lectura Recomendada**

https://flask.palletsprojects.com/en/1.1.x/config/

## Uso de Metodo Post en Flask-WTF
Si intentamos enviar la forma, saldra un error:

    Method Not Allowed
    The method is not allowed for the requested URL.

Es decir que hay un metodo que no esta permitido en esa ruta.

**Metodo GET and POST**

GET y POST son dos técnicas eficientes que pueden enviar los datos a un servidor o navegador y necesariamente que estos se comuniquen. Los dos métodos son distintos cuando el método GET añade los datos codificados a la URI, mientras que en el caso del método POST los datos se añaden al cuerpo y no a la URI. Además, se utiliza el método GET para recuperar los datos. Por el contrario, el método POST se utiliza para almacenar o actualizar los datos.

Cuando enviamos un POST como es el caso, no esta habilitado, y eso es lo que esta pasando. Mientras que *GET* esta habilitado por defecto, *POST* tiene que ser habilitado en la ruta manualmente, debemos habilitarlos al mismo tiempo.

Vamos agregar un parametro que es una lista de los metodos permitidos, en la ruta donde se hace uso de la forma.

    @app.route('/acceso', methods=['GET', 'POST'])
    def login():

Vuelve a correr el servidor, y al intentar enviar la forma, ya no dara error, pero simplemente no hara nada mas.

### Procesar la Forma para obtener los datos de la misma

La idea es obtener el *username* de la forma,  

Cuando nos hagen un *GET* se renderiza el formulario, pero cuando nos hagan un *POST* validamos que sea valido, y si asi lo es, obtenemos el *user_name*.

- Hacer uso del metodo *validate_on_submit()* de *FlaskForm*: *"And the convenient validate_on_submit will check if it is a POST request and if it is valid."*. Y obtenemos el *username* y lo guardamos en la session

        if loginform.validate_on_submit():
            username = loginform.username.data
            session['username'] = username


Recuerda obtenerlo de la session y enviarlo al contexto.

            username = session.get('username')

            context = {'loginform':loginform,
                'username':username,}


Para probar, en la misma ruta,  y dentro del template *acceso.html*, y haciendo uso del contexto de la aplicacion, mostramos el *username*

            {% if username%}
                 <h2>Bienvenido {{username}}</h2>
            {% endif%}

Nota, que tienes que enviar dos veces para que tome los cambios. 

<img src="https://i.imgur.com/SksH6DI.jpg" width="65%"/>

Sin embargo la logica del negocio, esta un poco extraña, porque lo mas logica seria que el usuario ingresara y lo llevara a otra ruta. En la siguiente haremos mejorar y actualizaciones.

## Mejorando la logia del negocio con GET and POST

Requerimientos: Que solo se pueda acceder a la ruta de consultas, siempre y cuando se haya identificado. Que me muestre la ruta de consultas mi nombre de usuario y siempre en mayusculas, y ojala en un container.

- importamos *url_for*, y retornamos la ruta. 

        from flask import Flask url_for
        ...
        ...
        return redirect(url_for('querries'))

- Quitamos del navbar.html la opcion de consultas. **Ya no va** 👇

        return redirect(url_for('querries'))     

- Modificar la ruta de consultas, y obtener el *username* de *session* y enviarlo al contexto:

        username = session.get('username')
        ...
        ...
            context = {'names':names,
               'languaje':languaje,
               'username':username,}

- Modificar el template de consultas para renderizar el *username*

        {% if username%}
            <h2>Bienvenido {{username}}</h2>
        {% endif%}

- Para que muestre siempre en mayusculas. Las variables que colocamos en doble corchete, tambien tienen filtros, y uno de ellos es *capitalize*, *upper* *lower*, entre otros, recomiendo esta lectura para profundizar:

https://www.codestudyblog.com/cnb/0624164113.html

        <h2>Bienvenido {{username | upper}}</h2>

- Dentro de un tag *div* de clase *container*, colocamos el codigo para qye muestre como una cajita.

        {% if username%}
            <div class="container">
                <h2>Bienvenido {{username | upper}}</h2>   
            </div>
        {% endif%}

## Desplegar Flashes (mensajes emergentes)

Es un banner que aparece abajo de la barra de navegacion. Estos mensajes son de informacion o ayuda al usuario, pueden ser de exito, fallo, o warning. Lo primero es importar:

    from flask import flash

1. Enviar el Flash: se debe importar *flash* de *flask*, y definir el mensaje, esto ultimo ira en la ruta login. y ahora la pregunta es ¿Como y en donde renderizar estos *flashes* en el *html?*

        from flask import flash
        ...
        ...
        flash('Username registrado con exito')

2. Vamos ahora a renderar los flashes en el html, modificamos el *base.html* porque queremos que los flashes se renderizen en cualquier pagina.

        <!-- renderizar flashes-->    
        {% for message in get_flashed_messages() %}
            <div class="alert alert-success alert-dismissible">
                <!--Se coloca un boton que permitira cerrar el flash, data-dismiss permitira cerrar la alerta-->
                <button type="button" 
                        data-dismiss="alert"
                        class="close">&times;</button>
                {{message}}
            </div>
        {% endfor %}


El codigo anterior, se coloco dentro del *block body* despues del *block navbar*. Para probar el codigo, corremos el servidor, vamos a *acceso* y posteriormente nos saldra un mensaje de *Username registrado con exito*

<img src="https://i.imgur.com/GVTZIxe.jpg" width="75%"/>

Sin embargo el mensaje anterior no se podra cerrar. Por Ahora solo voy a explicar el codigo anterior.

Un ciclo for 

- Dentro de un tag div usaremos tres clases: *alert*, *alert-success* y *alert-dismissible*, estas clases vienen de *Bootstrap*

- Dentro del tag *div* colocaremos un boton que permitira cerrar el flash. La propiedad *data-dismiss*, que tambien viene de *bootstrap*, permitira cerrar la alerta. 

- Se agregara la clase *close* y agregaremos una *x* que es *&times*


3. Falta agregar los scripts de *javascript*, iran en la parte de abajo del *body*

        <!-- importa los archivos javascript de bootstrap, y hereda, sin esto no se puede cerrar los flashes-->
        {% block scripts %}
            {{super()}}
        {% endblock%}

*Mas informacion:*
https://flask.palletsprojects.com/en/1.0.x/patterns/flashing/