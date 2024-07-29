from flask import Flask
from config import Config
from app.models import init_db

app = Flask(__name__)
app.config.from_object(Config)

with app.app_context():
    init_db()

from app import routes
