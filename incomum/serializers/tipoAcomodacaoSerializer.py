import re
from rest_framework import serializers
from ..models.tipoAcomodacao import TipoAcomodacao

class TipoAcomodacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoAcomodacao
        fields = '__all__'
