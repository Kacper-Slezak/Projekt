from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import DataRequired

class UploadForm(FlaskForm):
    file = FileField('Wybierz plik', validators=[DataRequired()])
    submit = SubmitField('Prześlij')