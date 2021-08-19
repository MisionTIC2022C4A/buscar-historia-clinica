from rest_framework import serializers
from .models import Attentions


class AttentionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('pacTipoId', 'pacNumId', 'pacNombre', 'servicio', 'profesional',)
        model = Attentions
