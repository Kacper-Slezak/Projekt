from flask import Flask
from config import Config
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config.from_object(Config)
app.config['WTF_CSRF_ENABLED'] = True

csrf = CSRFProtect(app)
from app import routes 
