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