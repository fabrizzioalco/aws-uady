from flask import Blueprint, request, jsonify
# from utils.validation import validate_professor_payload
from models import Profesor as ProfesorModel
from utils.validation import validate_professor_payload
from config import *
profesor_bp = Blueprint('profesor', __name__)


profesores=[]

@profesor_bp.route("/profesores", methods=["POST"])
def create_profesores():
	profesor_p = request.get_json()


	if not validate_professor_payload(profesor_p):
		return jsonify({"error": "BAD REQUEST"}), 400
	if ProfesorModel.query.filter_by(numeroEmpleado=profesor_p['numeroEmpleado']).first():
		return jsonify({"error": "Profesor con ID {id} ya existe"}), 400

	profesor = ProfesorModel(
		nombres=profesor_p['nombres'],
		apellidos=profesor_p['apellidos'],
		numeroEmpleado=profesor_p['numeroEmpleado'],
		horasClase=profesor_p['horasClase']
		)
	db.session.add(profesor)
	db.session.commit()

	return profesor.serialize(), 201

@profesor_bp.route("/profesores", methods=["GET"])
def get_profesores():
	profesores = ProfesorModel.query.all()
	response = dict() 

	for profesor in profesores:
		response.update(profesor.serialize())
	return response, 200

@profesor_bp.route("/profesores/<int:id>", methods=["PUT", "GET"])
def get_profesor(id):
	"""
	Obtiene un profesores
	"""
	profesor = ProfesorModel.query.filter_by(id=id).first_or_404(description='Profesor con ID {id} no existe')

	if request.method == "PUT":
		profesor_p = request.get_json()
		if not validate_professor_payload(profesor_p):
			return jsonify({"error": "BAD REQUEST"}), 400

		for key, value in request.get_json().items():
			setattr(profesor, key, value)
		db.session.commit()
		return profesor.serialize(), 200

		
	return profesor.serialize() , 200
@profesor_bp.route("/profesores/<int:id>", methods=["DELETE"])
def delete_profesores(id):
	"""
	Elimina un profesores
	"""	
	profesor = ProfesorModel.query.filter_by(id=id).first_or_404(description='Profesor con ID {id} no existe')
	db.session.delete(profesor)
	db.session.commit()
	return "", 200