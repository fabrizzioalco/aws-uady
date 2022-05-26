# from re import A
from flask import Blueprint, request, jsonify, abort
from utils.validation import validate_student_payload
from utils.s3 import push_to_s3
import boto3
# from app import *
from config import *
from werkzeug.utils import secure_filename
from models import Alumno as AlumnoModel





alumno_bp = Blueprint('alumno', __name__)
@alumno_bp.route('/alumno/<int:id>/fotoPerfil', methods=['POST'])
def save_profile_picture(id, request): 
	#Find the student to assign the url of the profile picture
	student = AlumnoModel.query.filter_by(id=alumno['id']).first_or_404()

	if 'foto' in request.files: 
		foto = request.files['foto']
		filename = secure_filename(foto.filename)
		foto.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		s3_url = upload_file(filename, 'alumnos')

		setattr(student, '')
		db.session.commit()

	return jsonify(student), 201


#GET
@alumno_bp.route("/alumnos", methods=["GET"])
def get_alumnos():

	students=AlumnoModel.query.all()
	print(students)

	#Print all of the students in a list
	return dict( [student.serialize() for student in students ])


@alumno_bp.errorhandler(405)
@alumno_bp.route("/alumnos/<int:id>", methods=["PUT", "GET"])
def get_alumno(id):
	"""
	Obtiene un alumno
	"""
	student = AlumnoModel.query.filter_by(id=id).first_or_404(description='Alumno con ID {id} no existe')

	if request.method == "PUT":
		if not validate_student_payload(request.get_json()):
			return jsonify({"error": "BAD REQUEST"}), 400

		for key, value in request.get_json().items():
			setattr(student, key, value)
		db.session.commit()

		return student.serialize(), 200

	return student.serialize(), 201

@alumno_bp.errorhandler(405)
@alumno_bp.route("/alumnos/<int:id>", methods=["DELETE"])
def delete_alumno(id):
	"""
	Elimina un alumno_bp

	"""
	student = AlumnoModel.query.filter_by(id=id).first_or_404(description='Alumno con ID {id} no existe')
	db.session.delete(student)
	db.session.commit()
	return 

@alumno_bp.errorhandler(405)
@alumno_bp.route("/alumnos", methods=["POST"])
def create_alumno():
	alumno = request.get_json()

	if AlumnoModel.query.filter_by(matricula=alumno["matricula"]).first():
		return jsonify({"error": "Alumno ya existe"}), 400

	student= AlumnoModel(
		nombre=alumno['nombre'],
		apellido=alumno['apellido'],
		matricula=alumno['matricula'],
		promedio=alumno['promedio']
	)
	db.session.add(student)
	db.session.commit()
	return student.serialize(), 201