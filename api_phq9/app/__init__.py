from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

from .phq_9 import phq9_bp
app.register_blueprint(phq9_bp)

from .user import user_bp
app.register_blueprint(user_bp)

from app import routes