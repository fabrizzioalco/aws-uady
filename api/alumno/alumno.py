from flask import Blueprint, request
from models import Alumno as alumno

alumno = Blueprint('alumno', __name__)
alumno_data=dict()

@alumno.route("/alumno", methods=["POST"])
def create_alumno():
	"""
	Crea un alumno
	"""


	return "Crear alumno"

#GET
@alumno.route("/alumnos", method=["GET"])
def get_alumnos():
	"""
	Obtiene todos los alumnos
	"""
	return "Obtener todos los alumnos"

@alumno.route("/alumonos/<int:id>", method=["PUT", "GET"])
def get_alumno(alumno):
	"""
	Obtiene un alumno
	"""

	if request.method == "PUT":
		return "Actualizar alumno"


	return "Obtener un alumno"

@alumno.route("alumnos/<int:id>", methods=["DELETE"])
def delete_alumno(id):
	"""
	Elimina un alumno
	"""
	return "Eliminar un alumno"