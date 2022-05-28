from api.alumno.alumno import alumno_bp
from api.profesor.profesor import profesor_bp
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import os 
import psycopg2
from config import *

basedir = os.path.abspath(os.path.dirname(__file__))



# app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI') or 'sqlite:///sicei-webS.db'
# app.config['UPLOAD_FOLDER'] = './upload'

# db = SQLAlchemy(app)
from models import *
#Register blueprints
app.register_blueprint(alumno_bp)
app.register_blueprint(profesor_bp)

