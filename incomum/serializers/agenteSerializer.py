from rest_framework import serializers
from ..models.agente import Agente

class AgenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agente
        fields = '__all__'
