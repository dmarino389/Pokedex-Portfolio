from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)  # Initialize SQLAlchemy with the app
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from app.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from app import routes
