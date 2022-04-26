from flask import Blueprint, request, jsonify
from utils.validation import validate_professor_payload
profesor_bp = Blueprint('profesor', __name__)

profesores=[]

@profesor_bp.route("/profesores", methods=["POST"])
def create_profesores():
	profesor_p = request.get_json()

	if not validate_professor_payload(profesor_p):
		return jsonify({"error": "BAD REQUEST"}), 400

	for profesor in profesores:
		if profesor_p["id"] == profesor["id"]:
			return jsonify({"error": "Already Exist"}), 400

	profesores.append(profesor_p)
	return jsonify(profesor_p), 201

@profesor_bp.route("/profesores", methods=["GET"])
def get_profesores():
	return jsonify(profesores), 200

@profesor_bp.route("/profesores/<int:id>", methods=["PUT", "GET"])
def get_profesor(id):
	"""
	Obtiene un profesores
	"""

	if request.method == "PUT":
		profesor_p = request.get_json()
		if not validate_professor_payload(profesor_p):
			return jsonify({"error": "BAD REQUEST"}), 400

		for profesor in profesores:
			if profesor["id"] == id:
				profesor["nombres"] = request.get_json().get('nombres')
				profesor["apellidos"] = request.get_json().get('apellidos')
				profesor["numeroEmpleado"] = request.get_json().get('numeroEmpleado')
				profesor["horasClase"] = request.get_json().get('horasClase')
				return jsonify(profesor), 200

	for profesor in profesores: 
		if profesor["id"] == id:
			return profesor, 200
		
	return  {}, 404
@profesor_bp.route("/profesores/<int:id>", methods=["DELETE"])
def delete_profesores(id):
	"""
	Elimina un profesores
	"""

	for profesor in profesores: 

		if profesor["id"] == id:
			profesores.remove(profesor)
			return {},200

	return {}, 404