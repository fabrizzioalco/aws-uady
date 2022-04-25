from flask import Blueprint, request
# from models import Alumno as alumno

alumno_bp = Blueprint('alumno', __name__)

alumnos=[]
@alumno_bp.route("/alumno", methods=["POST"])
def create_alumno():
	alumno = request.get_json()
	# print(alumno)
	alumnos.append(alumno)
	return "Crear alumno"

#GET
@alumno_bp.route("/alumnos", methods=["GET"])
def get_alumnos():
	"""
	Obtiene todos los alumno
	"""
	return "Obtener todos los alumno_bps"

@alumno_bp.route("/alumonos/<int:id>", methods=["PUT", "GET"])
def get_alumno(alumno):
	"""
	Obtiene un alumno
	"""

	if request.methods == "PUT":
		return "Actualizar alumno_bp"


	return "Obtener un alumno_bp"

@alumno_bp.route("/alumnos/<int:id>", methods=["DELETE"])
def delete_alumno(id):
	"""
	Elimina un alumno_bp
	"""
	return "Eliminar un alumno_bp"