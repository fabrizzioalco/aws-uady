import uuid
from app import db
class Alumno(db.Model): 
	id=db.Column(db.Integer, primary_key=True)
	apellido=db.Column(db.String(80), nullable=False)
	nombre=db.Column(db.String(80), nullable=False)
	matricula=db.Column(db.String(80), nullable=False)
	promedio=db.Column(db.Float, nullable=False)



class Profesor(db.Model):
	id=db.Column(db.Integer, primary_key=True)
	nombre=db.Column(db.String(80), nullable=False)
	apellido=db.Column(db.String(80), nullable=False)
	numeroEmpleado=db.Column(db.String(80), nullable=False)
	horasClase=db.Column(db.Integer, nullable=False)
