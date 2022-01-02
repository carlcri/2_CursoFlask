# export FLASK_APP=main.py
# export FLASK_DEBUG=1
# flask run


# importamos request
from flask import Flask, request

# se instancia un objeto de Flask, y se le da como parametro el nombre de la aplicacion que es main.py
app = Flask(__name__)


# con este decorador estamos dandole una ruta
@app.route('/')
def hello():
    user_ip = request.remote_addr
    return f'hello your ip is {user_ip}'