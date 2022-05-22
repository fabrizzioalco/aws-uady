from api.alumno.alumno import alumno_bp
from api.profesor.profesor import profesor_bp
from flask import Flask
from flasgger import Swagger
from flask_sqlalchemy import SQLAlchemy


# engine=db.create_engine('mysql+pymysql://root:root@localhost/universidad')
# engine.connect()


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/universidad'
db=SQLAlchemy(app)
#Register blueprints
app.register_blueprint(alumno_bp)
app.register_blueprint(profesor_bp)