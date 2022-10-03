import datetime
from Services.database_monoengine import db
import uuid
from flask_login import UserMixin
import mongoengine as me
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from wtforms.validators import DataRequired



class User(me.Document, UserMixin):
    name = me.StringField(required=True)
    email = me.StringField(required=True)
    password = me.StringField(required=True)
    date_created = me.DateTimeField(default=datetime.datetime.now())

    
       
    meta = {'collection': 'users', 'strict': False}
    
    def to_json(self):        
        return {"name": self.name,
                "email": self.email}
        
    def is_authenticated(self):
        return True

    def is_active(self):   
        return True           

    def is_anonymous(self):
        return False          

    def get_id(self):         
        return str(self.id)

#A form that can be usefull to update User model
class form_users_update(FlaskForm):


    label_name = StringField("Fullname: ")



    label_email = StringField("Email......:")




    label_password = StringField("Password: ")
    input_password = PasswordField("password", validators=[DataRequired(), validators.Length(min=8, max=18)])

    

