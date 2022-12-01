from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    email = db.Column(db.String(100), unique=True)
    date_joined = db.Column(db.Date, default = datetime.utcnow)
    
    def __repr__(self):
        return f'User > {self.name}, their email is {self.email}'

# for the working outside of application context error

# open the python shell
# from app import User, app, db
# app.app_context().push()

# then
  
# add a record to the data base
# example = User(name='example', email='example@example.com')
# db.session.add(example)
# db.session.commit()


another_example = User(name='Another_Example', email='anotherexample@farts.com')
db.session.add(another_example)
db.session.commit()