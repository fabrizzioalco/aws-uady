from re import U
from config import *


class Alumno(db.Model):
	__tablename__ = 'alumno'


	id = db.Column(db.Integer, primary_key=True)
	nombres = db.Column(db.String(100))
	apellidos = db.Column(db.String(100))
	matricula = db.Column(db.String(10), unique=True)
	promedio = db.Column(db.Float)
	fotoPerfilUrl = db.Column(db.String(100))

	def __init__(self, nombres, apellidos, matricula, promedio):
		self.nombres = nombres
		self.apellidos = apellidos
		self.matricula = matricula
		self.promedio = promedio
		self.fotoPerfilUrl = " "

	def __repr__(self):
		return '<Alumno %r>' % self.id


	def serialize(self):
		return {
			'id': self.id,
			'nombres': self.nombres,
			'apellidos': self.apellidos,
			'matricula': self.matricula,
			'promedio': self.promedio,
			'fotoPerfilUrl': self.fotoPerfilUrl
		}

class Profesor(db.Model):
	__tablename__='profesor'

	id = db.Column(db.Integer, primary_key=True)
	nombres=db.Column(db.String(80))
	apellidos=db.Column(db.String(80))
	numeroEmpleado=db.Column(db.String(80), unique=True)
	horasClase=db.Column(db.Integer)


	def __init__(self, nombres, apellidos, numeroEmpleado, horasClase):
		self.nombres = nombres
		self.apellidos = apellidos
		self.numeroEmpleado = numeroEmpleado
		self.horasClase = horasClase


	def __repr__(self):
		return '<Profesor %r>' % self.id


	def serialize(self):
		return {
			'id': self.id,
			'nombres': self.nombres,
			'apellidos': self.apellidos,
			'numeroEmpleado': self.numeroEmpleado,
			'horasClase': self.horasClase
		}

db.create_all()