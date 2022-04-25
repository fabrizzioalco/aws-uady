from api.alumno.alumno import alumno_bp
from flask import Flask
from flasgger import Swagger


app = Flask(__name__)
#Register blueprints
app.register_blueprint(alumno_bp)