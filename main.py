# se importa render_template
from flask import Flask, request, make_response, redirect, render_template

# se instancia un objeto de Flask, y se le da como parametro el nombre de la aplicacion que es main.py
app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(port=PORT, debug=DEBUG)