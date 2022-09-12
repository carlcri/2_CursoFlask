*Puedes consultar la aplicacion aqui:*

**https://miappflask.herokuapp.com/**

## Macros

Los *macros* son  pequenas piezas de codigo reutilizable. Crearemos un archivo llamado *macros.html* dentro de templates.

Para este caso, se crea un macro para renderizar una lista.

    {% macro render_list(my_list)%}
        {% for element in my_list %}
            <li>{{element}}</li>
        {% endfor %}   
    {% endmacro%}

## Include y Links

Crear una barra de navegacion dentro del *header*, a modo de lista. Esta barrita de navegacion contendra:
- ir a consultas
- ir a inicio(welcome)
- ir a un sitio externo, y abrirlo en una nueva instancia

Crearemos un nuevo template llamado *navbar.html*, y dentro creamos la barra de navegacion, con el tag *nav*

Dentro del tag *nav*, se crea una lista de elementos.

**Cambios en base.html**

Con el tag *header* lo creamos dentro del body.

El elemento de HTML Header representa un grupo de ayudas introductorias o de navegación. Puede contener algunos elementos de encabezado, así como también un logo, un formulario de búsqueda, un nombre de autor y otros componentes

Y lo vamos a incluir con este *stament*:

    {%include 'navbar.html'%}


## Uso de archivos estáticos: imágenes

Rendirazaremos una imagen de *ricky and Morthy* cuando no se encuentre la IP del usuario, y una segunda imagen en el *header* que sera un logo.

Creamos un nuevo directorio *Static* y dentro de el otro: *images*. 

En el template de *welcome.html* agregaremos esta linea de codigo:

    <img src="{{url_for('static', filename='images/ricky.jpg')}}" alt="ricky">

Se hace una referencia con *url_for* al archivo que se quiere cargar, en este caso, *url_for* en vez de la funcion de la ruta, apuntara al directorio *static*, y posteriormente el archivo.

Al renderizar la imagen, la muestra, sin embargo, muchas veces los archivos staticos se quedan guardados en el cache del browser, por lo que se recomienda, con un **HARD RELOAD** que va a depender del navegador usado. Para EDGE: 

    CTRL + F5

o

    (CTRL) + Fn + F5 on your keyboard.

Como la imagen esta un poco grande, y se quiere modificar su tamaño, se puede hacer mediante un archivo *.css*.

El main.css esta en el subdirectorio static/css/

    img{
    max-width: 30px;
    }

Y dentro de *base.html* en el *head*, con un tag de link, se hace referencia al base.html

    <link rel='stylesheet' href="{{ url_for('static', filename='css/main.css')}}">

**Ejercicio**

Renderizar el logo de platzi, para que aparezca en la barra de navegacion. Modificar *navbar.html*:


    <img src="{{url_for('static', filename='images/platzi.png')}}" alt="logo platzi">

## Configurar paginas de error

**Error 404**
¿Como manejar particularmente el error 404 cuando un usuario va alguna ruta que la aplicacion desconoce? 

Para que no aparezca como un error por defecto, vamos hacer uso la funcion de flask: *errorhandler*.

Como vez, *error_handler* en vez de recibir una ruta, recibe un codigo de error. La funcion decorada, recibe el error como parametro. Y enviamos en el contexto el error.

    @app.errorhandler(404)
        def not_found(error):
        return render_template('404.html', error=error)

**Error 500**
Error del servidor: lo simulamos con una ruta (/error), y lo manejamos en el main.py, casi igual con el error anterior.

Desactiva el *modo debug* para poder realizar la practica.
