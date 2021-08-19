
import requests
import json

url = 'https://patient-ms.herokuapp.com/patient'

def cons_pac(numId, tipoId):
    g_url = url + '/' + numId + '/' + tipoId
    try:
        response = requests.get(g_url)
        resp = response.json()
        numId = resp.get('numeroIdentificacion', False) #Verificación
    except:
        resp = None
        numId = False
    status = (numId != False)
    return status, resp


def nuevo_paciente():
    headers = { 'Content-type': 'application/json'}
	
    body = {'numeroIdentificacion': '123456',
			'tipoIdentificacion': 'CC',
			'nombreCompleto': 'Maria Gomez',
			'fechaNacimiento': '1999-03-13',
			'estadoCivil': 'Soltero',
			'ocupacion': 'Ama de casa',
			'direccion': 'Calle 15 N 7-12',
			'ciudad': 'Bogotá',
			'telefono': '310123456', 
			'email': 'maria@mail.com',
			'nombreAcompanante': '',
			'aseguradora': 'EPS Sura',
			'vinculacion': 'Afiliado',
			'fechaIngreso': '2021-08-18',
			}

    response = requests.post(url, headers=headers, data=json.dumps(body))
    resp = response.json()
    print('*********************************')
    print(resp)
    return resp
