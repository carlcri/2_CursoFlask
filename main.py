from flask import Flask, request, make_response, redirect, render_template, session

from data_workers import DATA
from flask_bootstrap import Bootstrap

fruits = ['banana', 'apple', 'orange', 'cherry']

app = Flask(__name__)
bootstrap = Bootstrap(app)

# esta propiedad configura la llave secreta
app.config['SECRET_KEY']='ubuntu'

@app.route('/')
def index():
    user_ip = request.remote_addr
    session['user_ip']=user_ip
    response = make_response(redirect('/hello'))

    return response

# Obtiene una lista de acuerdo a la condicion
def get_list():
    python_dev_list = list(filter(lambda worker : worker['language'] == 'python', DATA))
    python_dev_list = list(map(lambda worker: worker['name'], python_dev_list))

    return python_dev_list


# se crea un diccionario con los parametros que vamos a pasar
# la notacion **context, nos permite expandir el diccionario
@app.route('/hello')
def hello():
    user_ip = session.get('user_ip')
    user_name='facundo'
    python_dev_list = get_list()
    
    context ={
        'user_ip':user_ip,
        'user_name':user_name,
        'fruits':fruits,
        'python_dev_list':python_dev_list,
    }
    return render_template('hello.html', **context )


@app.route('/atravesados')
def atravesados():
    return render_template('atravesados.html')


@app.route('/error')
def internal_error():
    1/0


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html', error=error)
