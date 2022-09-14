from flask import Flask
from flask_bootstrap import Bootstrap

def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app=app)

    # Se hace uso del atributo config de FLASK para generar una llave secreta
    app.config['SECRET_KEY'] = 'misecreto'

    return app
    