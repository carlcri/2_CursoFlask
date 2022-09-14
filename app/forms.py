
from flask_wtf import FlaskForm
from wtforms.fields import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired

# extendemos la clase FlaskForm. Lo que esta entre parentesis se concoce como etiquetas
# Se integra el validador DataRequired
class LoginForm(FlaskForm):
    username = StringField('Nombre de Usuario', validators=[DataRequired()])
    password = PasswordField('contraseña', validators=[DataRequired()])
    submit = SubmitField('Enviar')