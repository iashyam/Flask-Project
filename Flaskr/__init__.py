from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#creatung the base app
app = Flask(__name__)

app.config['SECRET_KEY'] = '1dee4de2f1e0017b7aba8b5b8b2e4280'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cite.db'

db = SQLAlchemy(app)

from Flaskr.database import User, Post