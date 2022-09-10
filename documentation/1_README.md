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




