from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, IntegerField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange



class AddPetForm(FlaskForm):
    name = StringField("Pet Name",  validators=[InputRequired(message="Pet Name can't be blank")])
    # we can change this to add choices dynamically
    species = SelectField("Species", choices=[('cat', 'cat'),  ('dog', 'dog'),  ('porcupine', 'porcupine')])  
    photo_url = StringField("Photo URL", validators=[URL(message="Please enter correct URL"), Optional()], default="https://images.unsplash.com/photo-1568640347023-a616a30bc3bd?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1052&q=80")
    age = IntegerField("Age (0..30) months", validators=[Optional(), NumberRange(min=0, max=30, message = "Age should be in range 0..30")])
    notes = TextAreaField("Additional Info", validators=[Optional()])
    
    # how to display like a checkbox and change value?
    available = BooleanField('Available', default="checked")

class EditPetForm(FlaskForm):   
    photo_url = StringField("Photo URL", validators=[URL(message="Please enter correct URL"), Optional()], default="https://images.unsplash.com/photo-1568640347023-a616a30bc3bd?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1052&q=80")
    age = IntegerField("Age (0..30) months", validators=[Optional(), NumberRange(min=0, max=30, message = "Age should be in range 0..30")])
    notes = TextAreaField("Additional Info", validators=[Optional()])
    
    # how to display like a checkbox and change value?
    available = BooleanField('Available', default="checked")
