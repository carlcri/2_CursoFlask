# se importa make_response, redirect
from flask import Flask, request, make_response, redirect

# se instancia un objeto de Flask, y se le da como parametro el nombre de la aplicacion que es main.py
app = Flask(__name__)

DEBUG = False
PORT = 5000


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
    return f'Welcome your ip is: {user_ip}'        


if __name__ == '__main__':
    app.run(port=PORT, debug=DEBUG)