from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email


class Contactform(FlaskForm):
    name = StringField('Name ', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    sub= StringField('Subject', validators=[DataRequired()])
    body = StringField('Message', validators=[DataRequired()])