from flask import Blueprint, request
# from models import Alumno as alumno

alumno_bp = Blueprint('alumno', __name__)

alumnos=[]
@alumno_bp.route("/alumno", methods=["POST"])
def create_alumno():
	alumno = request.get_json()
	# print(alumno)

	#TODO: Create validation. And create from model
	alumnos.append(alumno)
	print(alumnos)
	return alumno

#GET
@alumno_bp.route("/alumnos", methods=["GET"])
def get_alumnos():
	return alumnos

@alumno_bp.route("/alumno/<int:id>", methods=["PUT", "GET"])
def get_alumno(id):
	"""
	Obtiene un alumno
	"""
	alumno_id = request.get_json().get('id')

	if request.method == "PUT":
		return "Actualizar alumno_bp"

	for student in alumnos: 
		if student["id"] == alumno_id:
			return student
		else:
			return "No existe alumno_bp con id: {}".format(alumno_id)

@alumno_bp.route("/alumnos/<int:id>", methods=["DELETE"])
def delete_alumno(id):
	"""
	Elimina un alumno_bp
	"""
	return "Eliminar un alumno_bp"