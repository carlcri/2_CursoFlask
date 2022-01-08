from flask import Flask, request, make_response, redirect, render_template, session, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired


fruits = ['banana', 'apple', 'orange', 'cherry']


app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'password'


class LoginForm(FlaskForm):
    username = StringField('Nombre de Usuario', validators=[DataRequired()])
    password = PasswordField('contrasena', validators=[DataRequired()])
    submit = SubmitField('Enviar')


@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))

    # Guardamos el user_ip en session
    session['user_ip'] = user_ip

    return response


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    # obteniendo user_ip y user_name directamente de la session 
    user_ip = session.get('user_ip')
    user_name = session.get('user_name')
    login_form = LoginForm()

    context ={
        'user_ip':user_ip,
        'user_name':user_name,
        'fruits':fruits,
        'login_form': login_form,  
    }
    if login_form.validate_on_submit():
        user_name = login_form.username.data
        session['user_name'] = user_name

        flash('nombre de usuario registrado con exito')

        return redirect(url_for('index'))

    return render_template('hello.html', **context)

@app.route('/error')
def internal_error():
    1/0


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html', error=error)
