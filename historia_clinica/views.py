from django.shortcuts import render

from django.views import View
from .models import Attentions
from .serializer import AttentionSerializer
from django.http import JsonResponse
from .patient_util import cons_pac, nuevo_paciente
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from datetime import date, datetime


@api_view(['POST'])
def attentions_create(request):
    if request.method == 'POST':
        attention_data = JSONParser().parse(request)
        sts, paciente = cons_pac(
            attention_data['pacNumId'], attention_data['pacTipoId'])
        if sts:
            attention_data['pacNombre'] = paciente['nombreCompleto']
        else:
            return JsonResponse({'message': 'Paciente no existe'})
        attention_serializer = AttentionSerializer(data=attention_data)
        if attention_serializer.is_valid():
            attention_serializer.save()
            return JsonResponse(attention_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(attention_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def attentions_day(request, day=None):
    if request.method == 'GET':
        if not day:
            day = date.today()
        attentions = Attentions.objects.filter(fechaCreacion__date=day)
        attentions_serializer = AttentionSerializer(attentions, many=True)
        return JsonResponse(attentions_serializer.data, safe=False)


@api_view(['GET'])
def attentions_pac(request, tipoId,  numId):
    if request.method == 'GET':
        attentions = Attentions.objects.filter(
            pacTipoId=tipoId, pacNumId=numId)
        attentions_serializer = AttentionSerializer(attentions, many=True)
        return JsonResponse(attentions_serializer.data, safe=False)


@api_view(['GET', 'DELETE'])
def attentions_list(request):
    if request.method == 'GET':
        attentions = Attentions.objects.all()
        attentions_serializer = AttentionSerializer(attentions, many=True)
        return JsonResponse(attentions_serializer.data, safe=False)

    elif request.method == 'DELETE':
        count = Attentions.objects.all().delete()
        return JsonResponse({'message': 'Todas las atenciones ({}) se borraron correctamente!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


'''
class PatientView(View):
	def get(self, request):
		print(f'---------GET---------{request}---------------------------')
		tipoId = request.GET['tipoId']
		numId = request.GET['numId']
		#patient = Patient.objects.get(pk=pk)
		patient = Patient.objects.get(numero_identificacion=numId, tipo_identificacion=tipoId)
		data = {}
		data['nombre'] = patient.nombre_completo
		data['id'] = patient.numero_identificacion
		data['tipoId'] = patient.tipo_identificacion
		
		return JsonResponse(data)
'''
