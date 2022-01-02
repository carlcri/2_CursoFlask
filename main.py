# export FLASK_APP=main.py
# export FLASK_DEBUG=1
# flask run


# se importa make_response, redirect
from flask import Flask, request, make_response, redirect

# se instancia un objeto de Flask, y se le da como parametro el nombre de la aplicacion que es main.py
app = Flask(__name__)

# ruta raiz
@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)

    return response



# ruta hello
@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    return f'hello your ip is: {user_ip}'