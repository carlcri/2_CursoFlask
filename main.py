from flask import Flask, request, make_response, redirect, render_template

fruits = ['banana', 'apple', 'orange', 'cherry']

app = Flask(__name__)


@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)

    return response


# se crea un diccionario con los parametros que vamos a pasar
# la notacion **context, nos permite expandir el diccionario
@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    context ={
        'user_ip':user_ip,
        'fruits':fruits,
    }
    return render_template('hello.html', **context )