

def validate_student_payload(payload): 
	"""
	Validates the payload
	"""
	if payload is None:
		return False
	if 'nombres' not in payload:
		return False
	if 'apellidos' not in payload :
		return False
	if 'matricula' not in payload :
		return False
	if 'promedio' not in payload  :
		return False
	if type(payload["nombres"]) is not str:
		return False
	if type(payload["apellidos"]) is not str:
		return False
	if type(payload["matricula"]) is not str:
		return False
	if type(payload["promedio"]) is not float:
		return False
	if payload["promedio"] < 0 or payload["promedio"] > 10:
		return False
	if payload["matricula"] == "":
		return False
	if payload["nombres"] == "":
		return False
	if payload["apellidos"] == "":
		return False
	if payload["matricula"] is None:
		return False
	if payload["promedio"] is None:
		return False
	if payload['apellidos'] is None:
		return False
	if payload['nombres'] is None:
		return False
	return True


def validate_professor_payload(payload):
	"""
	Validates the payload
	"""
	if payload is None:
		return False
	if type(payload) is not dict:
		return False
	if 'nombres' not in payload or None:
		return False
	if 'apellidos' not in payload or None:
		return False
	if 'numeroEmpleado' not in payload or None:
		return False
	if 'horasClase' not in payload or None:
		return False
	if type(payload["nombres"]) is not str:
		return False
	if type(payload["apellidos"]) is not str:
		return False
	if type(payload["numeroEmpleado"]) is not int:
		return False
	if type(payload["horasClase"]) is not int:
		return False
	if payload["numeroEmpleado"] < 0:
		return False
	if payload["horasClase"] < 0:
		return False
	if payload["nombres"] == "":
		return False
	if payload["apellidos"] == "":
		return False
	if payload["nombres"] is None:
		return False
	if payload["apellidos"] is None:
		return False
	if payload["numeroEmpleado"] is None:
		return False
	if payload["horasClase"] is None:
		return False
	return True
