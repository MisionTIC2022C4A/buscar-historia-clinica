from rest_framework import serializers
from .models import Patient


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']