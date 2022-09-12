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
