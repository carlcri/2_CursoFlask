from flask import Flask, request, make_response, redirect, render_template
from data_workers import DATA

fruits = ['banana', 'apple', 'orange', 'cherry']

app = Flask(__name__)


@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)

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
    user_ip = request.cookies.get('user_ip')
    python_dev_list = get_list()
    
    context ={
        'user_ip':user_ip,
        'fruits':fruits,
        'python_dev_list':python_dev_list,
    }
    return render_template('hello.html', **context )