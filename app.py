from api.alumno.alumno import alumno_bp
from api.profesor.profesor import profesor_bp
from flask import Flask
from flasgger import Swagger


app = Flask(__name__)
#Register blueprints
app.register_blueprint(alumno_bp)
app.register_blueprint(profesor_bp)