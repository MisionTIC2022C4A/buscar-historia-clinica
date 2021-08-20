from django.urls import path, include
from .views import *
urlpatterns = [
	path('nueva_atencion', attentions_create),
	path('atenciones/', attentions_list),
	path('atenciones_dia/<day>', attentions_day),
	path('atenciones_dia/', attentions_day),
	path('atenciones_pac/<tipoId>/<numId>', attentions_pac),
]