import re
from rest_framework import serializers
from ..models.situacaoTuristico import SituacaoTuristico

class SituacaoTuristicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SituacaoTuristico
        fields = '__all__'
