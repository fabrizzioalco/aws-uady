from flask import Blueprint, request, jsonify

profesor_bp = Blueprint('profesor', __name__)

profesores=[]

@profesor_bp.route("/profesor", methods=["POST"])
def create_profesor():
	profesor = request.get_json()

	if profesor["id"] in profesores:
		return jsonify({"error": "profesor already exists"}), 400

	profesores.append(profesor)
	print(profesores)
	return profesor, 200

@profesor_bp.route("/profesores", methods=["GET"])
def get_profesores():
	return jsonify(profesores), 200

@profesor_bp.route("/profesor/<int:id>", methods=["PUT", "GET"])
def get_profesor(id):
	"""
	Obtiene un profesor
	"""
	profesor_id = request.get_json().get('id')

	if request.method == "PUT":
		for profesor in profesores:
			if profesor["id"] == profesor_id:
				profesor["nombre"] = request.get_json().get('nombre')
				profesor["apellido"] = request.get_json().get('apellido')
				profesor["numeroEmpleado"] = request.get_json().get('numeroEmpleado')
				profesor["horasClase"] = request.get_json().get('horasClase')
				return jsonify(profesor), 200

	for profesor in profesores: 
		if profesor["id"] == profesor_id:
			return profesor, 200
		else:
			return "No existe profesor con id: {}".format(profesor_id), 404

@profesor_bp.route("/profesor/<int:id>", methods=["DELETE"])
def delete_profesor(id):
	"""
	Elimina un profesor
	"""
	profesor_id = request.get_json().get('id')

	for profesor in profesores: 
		if profesor["id"] == profesor_id:

			profesores.remove(profesor)
			return "Profesor eliminado", 200

	return "No existe profesor con id: {}".format(profesor_id), 404