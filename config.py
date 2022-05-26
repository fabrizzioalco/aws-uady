from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask import Flask
import os 


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI') or 'sqlite:///sicei-webS.db'
app.config['UPLOAD_FOLDER'] = './upload'

db = SQLAlchemy(app)