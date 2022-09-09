from flask import Flask, request

# se instancia un objeto de Flask, y se le da como parametro el nombre de la aplicacion que es main.py
app = Flask(__name__)

DEBUG = False
PORT = 5000


# con este decorador estamos dandole una ruta
@app.route('/')
def index():
    user_ip = request.remote_addr
    return f'Hello your ip is: {user_ip}'

if __name__ == '__main__':
    app.run(port=PORT, debug=DEBUG)