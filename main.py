# export FLASK_APP=main.py
# export FLASK_DEBUG=1
# flask run

from flask import Flask

# se instancia un objeto de Flask, y se le da como parametro el nombre de la aplicacion que es main.py
app = Flask(__name__)


# con este decorador estamos dandole una ruta
@app.route('/')

def hello():
    return 'Hola como estan: estamos congelados'