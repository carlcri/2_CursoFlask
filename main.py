# Se importa la clase Bootstrap
import random
from flask import Flask, request, make_response, redirect, render_template
from data.DataWorkers import DATA, get_worker_by_languaje
from flask_bootstrap import Bootstrap

# se crea una instancia de Bootstrap y se le pasa como parametro una aplicacion de Flask
app = Flask(__name__)
bootstrap = Bootstrap(app=app)

DEBUG = False
PORT = 5000


fruits = ['Banana', 'Apple', 'Orange', 'Cherry']

# Ruta Raiz
@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/welcome'))
    response.set_cookie('user_ip', user_ip)
    
    return response


# Ruta Welcome
@app.route('/welcome')
def welcome():
    user_ip = request.cookies.get('user_ip')
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


if __name__ == '__main__':
    app.run(port=PORT, debug=DEBUG)