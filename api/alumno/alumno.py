from flask import Blueprint, request, jsonify
# from models import Alumno as alumno

alumno_bp = Blueprint('alumno', __name__)

alumnos=[]
@alumno_bp.route("/alumno", methods=["POST"])
def create_alumno():
	alumno = request.get_json()
	#TODO: Create validation. And create from model
	if alumno["id"] in alumnos:
		return jsonify({"error": "alumno already exists"}), 400

	alumnos.append(alumno)
	print(alumnos)
	return alumno, 200

#GET
@alumno_bp.route("/alumnos", methods=["GET"])
def get_alumnos():
	return jsonify(alumnos), 200

@alumno_bp.route("/alumno/<int:id>", methods=["PUT", "GET"])
def get_alumno(id):
	"""
	Obtiene un alumno
	"""
	alumno_id = request.get_json().get('id')

	if request.method == "PUT":
		for student in alumnos:
			if student["id"] == alumno_id:
				student["nombre"] = request.get_json().get('nombre')
				student["apellido"] = request.get_json().get('apellido')
				student["matricula"] = request.get_json().get('matricula')
				student["promedio"] = request.get_json().get('promedio')
				return jsonify(student), 200

	for student in alumnos: 
		if student["id"] == alumno_id:
			return student, 200
		else:
			return "No existe alumno_bp con id: {}".format(alumno_id), 404

@alumno_bp.route("/alumno/<int:id>", methods=["DELETE"])
def delete_alumno(id):
	"""
	Elimina un alumno_bp

	"""
	alumno_id = request.get_json().get('id')

	for student in alumnos: 
		if student["id"] == alumno_id:

			alumnos.remove(student)
			return "Alumno eliminado", 200

	return "No existe alumno_bp con id: {}".format(alumno_id), 404