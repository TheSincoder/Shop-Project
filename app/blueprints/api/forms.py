from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from ...models import User

class ItemForm(FlaskForm):
    #field name = DatatypeField('Label', validators=[LIST OF validators])
    name = StringField('Name', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    desc = StringField('Description', validators=[DataRequired()])
    img = StringField('Image', validators=[DataRequired()])
    category = StringField('Category', validators=[DataRequired()])
    submit = SubmitField('Create Item')


 