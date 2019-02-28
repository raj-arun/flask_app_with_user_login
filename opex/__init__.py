
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)

app.config['SECRET_KEY'] = '3c69b36a828b8c3d2954921ed15bddbe'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///opex.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from opex import routes