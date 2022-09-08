from flask import Flask

# se instancia un objeto de Flask, y se le da como parametro el nombre de la aplicacion que es main.py
app = Flask(__name__)

DEBUG = False
PORT = 5000


# con este decorador estamos dandole una ruta
@app.route('/')
def index():
    return 'Hello World, You are playing with fire'

if __name__ == '__main__':
    app.run(port=PORT, debug=DEBUG)