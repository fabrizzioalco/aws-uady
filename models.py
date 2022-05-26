import uuid
from app import db
from sqlalchemy.dialects.postgresql import JSON ,UUID
class Alumno(db.Model): 
	__tablename__ = 'alumno'

	id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
	apellido=db.Column(db.String(80), nullable=False)
	nombre=db.Column(db.String(80), nullable=False)
	matricula=db.Column(db.String(80), nullable=False)
	promedio=db.Column(db.Float, nullable=False)


	def __init__(self, apellido, nombre, matricula, promedio):
		self.apellido = apellido
		self.nombre = nombre
		self.matricula = matricula
		self.promedio = promedio
	
	def __repr__(self):
		return '<Alumno %r>' % self.id



class Profesor(db.Model):
	__tablename__='profesor'

	id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
	nombre=db.Column(db.String(80), nullable=False)
	apellido=db.Column(db.String(80), nullable=False)
	numeroEmpleado=db.Column(db.String(80), nullable=False)
	horasClase=db.Column(db.Integer, nullable=False)


	def __init__(sefl, nombre, apellido, numeroEmpleado, horasClase):
		self.nombre = nombre
		self.apellido = apellido
		self.numeroEmpleado = numeroEmpleado
		self.horasClase = horasClase


	def __repr__(self):
		return '<Profesor %r>' % self.id
