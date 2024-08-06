from rest_framework import serializers
from ..models.agencia import Agencia

class AgenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agencia
        fields = '__all__'