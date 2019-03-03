
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)

app.config['SECRET_KEY'] = '3c69b36a828b8c3d2954921ed15bddbe'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///opex.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  #used to redirect to the login page
login_manager.login_message_category = 'info'

from opex import routes