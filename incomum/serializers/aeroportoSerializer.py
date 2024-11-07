from rest_framework import serializers
from ..models.aeroporto import Aeroporto

class AeroportoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aeroporto
        fields = '__all__'
