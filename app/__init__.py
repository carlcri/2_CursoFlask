from flask import Flask
from flask_bootstrap import Bootstrap
from .config import Config

def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app=app)

    # Se modifica el atributo config de FLASK desde la clase Config
    app.config.from_object(Config)

    print('aplicacion creada')

    return app
    