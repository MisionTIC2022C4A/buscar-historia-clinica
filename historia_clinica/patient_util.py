
import requests

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