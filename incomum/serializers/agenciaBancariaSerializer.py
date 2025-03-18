from rest_framework import serializers
from ..models.agenciaBancaria import AgenciaBancaria

class AgenciaBancariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgenciaBancaria
        fields = '__all__'
