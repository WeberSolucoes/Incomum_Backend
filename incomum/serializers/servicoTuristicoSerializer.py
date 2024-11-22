import re
from rest_framework import serializers
from ..models.servicoTuristico import ServicoTuristico

class ServicoTuristicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicoTuristico
        fields = '__all__'
