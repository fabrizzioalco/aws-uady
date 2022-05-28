# from re import A
from botocore.config import Config
from curses import reset_prog_mode
from flask import Blueprint, request, jsonify, abort
from psycopg2 import Date
from utils.validation import validate_student_payload
from utils.s3 import push_to_s3
import boto3
import botocore 
from botocore.exceptions import ClientError
# from app import *
from config import *
from werkzeug.utils import secure_filename
from models import Alumno as AlumnoModel

bucket_name = 'pf-webs-s3'

alumno_bp = Blueprint('alumno', __name__)
@alumno_bp.route('/alumnos/<int:id>/fotoPerfil', methods=['POST'])
def save_profile_picture(id): 
	#Find the student to assign the url of the profile picture
	student = AlumnoModel.query.filter_by(id=id).first_or_404()
	print("This is the student", student)
	if 'foto' in request.files: 
		foto = request.files['foto']
		print(foto)
		print(os.getcwd())
		filename = secure_filename(foto.filename)
		print(filename)
		foto.save(os.path.join('./upload', filename))
	#	s3_url = push_to_s3(filename, bucket_name , student.nombres)
		s3_client = boto3.client('s3', aws_access_key_id='ASIASDXOW6JFGEXP75EF',
    					aws_secret_access_key='Izs949qQ+3moRGNIodCxOwyjk66Ef9lRKpKG4Euw',
    					aws_session_token='FwoGZXIvYXdzEAQaDOLz64DwytddibVQyyLJAYnqcaJRS6CyuSncdQw7u7E6IK4cDV+4Pdaf0hgXyiZp5dTOAimWEQBSFWuV3v7FzIgIo4Hr9muKDa+ckGOTy9M7tmX+GSoKIDyOFc4Lp0gFQH3OQI+XwnNhbvh83DiLwY2gvKX0rhBmMajl5NOztpfnEG6XgG0eU5zguBC2liOGM1f35xhdm5GbBeukIJkkNI6uUr7Jqao730ziKQS2LL61xx3bpdoNqwutoTNvKvQzx/onxt399DYeSoXm4U2wr/4Yw4Dd8WcRwyjTz8mUBjItYZC6ylNm/CNIpyDqGMkeJK3efJjWt0+1uu94fNsH6q9ruaCRp2jKzUKle44Y')
		try:
            		s3_client.upload_file(
                		'./upload/' + filename,
                		bucket_name,
               			student.nombres,
                		ExtraArgs={'ACL': 'public-read',
                           		"ContentType": filename})
		except ClientError as e:
			 return e

		config = Config(signature_version=botocore.UNSIGNED)
		fotoUrl = boto3.client('s3', config=config) \
            				.generate_presigned_url(
            				'get_object',
            				ExpiresIn=0,
            				Params={'Bucket': bucket_name, 'Key': student.nombres})
		setattr(student, 'fotoPerfilUrl', fotoUrl)
		db.session.commit()

	return student.serialize(), 200


#GET
@alumno_bp.route("/alumnos", methods=["GET"])
def get_alumnos():

	students=AlumnoModel.query.all()
	response=dict()
	for student in students:
		response.update(student.serialize())

	return response



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

	return student.serialize(), 200

@alumno_bp.errorhandler(405)
@alumno_bp.route("/alumnos/<int:id>", methods=["DELETE"])
def delete_alumno(id):
	"""
	Elimina un alumno_bp
	"""
	student = AlumnoModel.query.filter_by(id=id).first_or_404(description='Alumno con ID {id} no existe')
	db.session.delete(student)
	db.session.commit()
	return "", 200

@alumno_bp.errorhandler(405)
@alumno_bp.route("/alumnos", methods=["POST"])
def create_alumno():
	alumno = request.get_json()

	if not validate_student_payload(alumno):
		print(alumno)
		return jsonify({"error": "BAD REQUEST"}), 400

	if AlumnoModel.query.filter_by(matricula=alumno["matricula"]).first():
		return jsonify({"error": "Alumno ya existe"}), 400

	student= AlumnoModel(
		nombres=alumno['nombres'],
		apellidos=alumno['apellidos'],
		matricula=alumno['matricula'],
		promedio=alumno['promedio']
	)

	# student = AlumnoModel(
	# 	args['nombres'],
	# 	args['apellidos'],
	# 	args['matricula'],
	# 	args['promedio']
	# )
	db.session.add(student)
	db.session.commit()
	return student.serialize(), 201
