# se importa render_template
from flask import Flask, request, make_response, redirect, render_template


app = Flask(__name__)

# ruta raiz
@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)

    return response



# ruta hello, donde ahora en vez de retorna una cadena, retornamos el template: hello.html
# tambien enviamos 
@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    return render_template('hello.html', user_ip=user_ip)