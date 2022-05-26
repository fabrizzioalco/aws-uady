from re import U
from uuid import uuid4

# from click import UUID
from config import *
from sqlalchemy.dialects.postgresql import UUID

class Alumno(db.Model):
	__tablename__ = 'alumno'

	id = db.Column(db.Integer, primary_key=True)
	apellido = db.Column(db.String(80), nullable=False)
	nombre = db.Column(db.String(80), nullable=False)
	matricula = db.Column(db.String(80), nullable=False)
	promedio = db.Column(db.Float, nullable=False)
	fotoPerfiUrl = db.Column(db.String(80))

	def __init__(self, nombre, apellido, matricula, promedio):
		self.apellido = apellido
		self.id = self.id
		self.nombre = nombre
		self.matricula = matricula
		self.promedio = promedio
		self.fotoPerfilUrl = ""

	def __repr__(self):
		return '<Alumno %r>' % self.id


	def serialize(self):
		return {
			'id': self.id,
			'nombre': self.nombre,
			'apellido': self.apellido,
			'matricula': self.matricula,
			'promedio': self.promedio,
			'fotoPerfilUrl': self.fotoPerfilUrl
		}

class Profesor(db.Model):
	__tablename__='profesor'

	id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
	nombre=db.Column(db.String(80), nullable=False)
	apellido=db.Column(db.String(80), nullable=False)
	numeroEmpleado=db.Column(db.String(80), nullable=False)
	horasClase=db.Column(db.Integer, nullable=False)


	def __init__(sefl, nombre, apellido, numeroEmpleado, horasClase):
		self.id = uuid4()
		self.nombre = nombre
		self.apellido = apellido
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