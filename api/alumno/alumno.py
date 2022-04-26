from flask import Blueprint, request, jsonify, abort
from utils.validation import validate_student_payload
# from models import Alumno as alumno

alumno_bp = Blueprint('alumno', __name__)

alumnos=[]

@alumno_bp.errorhandler(405)
@alumno_bp.route("/alumnos", methods=["POST"])
def create_alumno():
	alumno = request.get_json()

	if not validate_student_payload(alumno):
		return jsonify({"error": "BAD REQUEST"}), 400

	for student in alumnos:
		if student["id"] == alumno["id"]:
			return jsonify({"error": "alumno already exists"}), 400

	alumnos.append(alumno)
	return alumno, 201

#GET
@alumno_bp.route("/alumnos", methods=["GET"])
def get_alumnos():
	return jsonify(alumnos), 200
@alumno_bp.errorhandler(405)
@alumno_bp.route("/alumnos/<int:id>", methods=["PUT", "GET"])
def get_alumno(id):
	"""
	Obtiene un alumno
	"""

	if request.method == "PUT":
		if not validate_student_payload(request.get_json()):
			return jsonify({"error": "BAD REQUEST"}), 400

		for student in alumnos:
			if student["id"] == id:
				student["nombres"] = request.get_json().get('nombres')
				student["apellidos"] = request.get_json().get('apellidos')
				student["matricula"] = request.get_json().get('matricula')
				student["promedio"] = request.get_json().get('promedio')
				return jsonify(student), 200

	for student in alumnos:
		if student["id"] == id:
			return student, 200

	return abort(404)

@alumno_bp.errorhandler(405)
@alumno_bp.route("/alumnos/<int:id>", methods=["DELETE"])
def delete_alumno(id):
	"""
	Elimina un alumno_bp

	"""
	for student in alumnos:
		if student["id"] == id:

			alumnos.remove(student)
			return "Alumno eliminado", 200

	return abort(404)