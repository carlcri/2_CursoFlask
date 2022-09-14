import random
from flask import Flask, request, make_response, redirect, render_template
from flask import session
from data.DataWorkers import DATA, get_worker_by_languaje
from flask_bootstrap import Bootstrap

# importamos la funcion para crear la aplicacion y la forma
from app import create_app
from app.forms import LoginForm

# Se crea la app
app = create_app()

#DEBUG = False
#PORT = 5000


fruits = ['Banana', 'Apple', 'Orange', 'Cherry']

# Ruta Raiz- Se Guarda el user_ip en el objeto session
@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/welcome'))
    session['user_ip'] = user_ip
    
    return response


# Ruta Welcome - Se obtiene la user_ip del objeto session
@app.route('/welcome')
def welcome():
    user_ip = session.get('user_ip')
    context = {'user_ip':user_ip,
                'fruits':fruits,}

    return render_template('welcome.html', **context)       


# Ruta Consultas
@app.route('/consultas')
def querries():
    languaje = random.choice(['python', 'java', 'ruby', 'javascript'])
    names = get_worker_by_languaje(languaje)
    context = {'names':names,
               'languaje':languaje,}

    return render_template('consultas.html', **context)

# Ruta Acceso
@app.route('/acceso')
def login():
    # se instancia un objeto de clase LoginForm
    loginform = LoginForm()
    context = {'loginform':loginform}

    return render_template('acceso.html', **context)


# Ruta Error Handler 404 
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


# Ruta para generar error
@app.route('/error')
def internal_error():
    1/0


# Ruta Error Handler 500
@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error) 


#if __name__ == '__main__':
#    app.run(port=PORT, debug=DEBUG)