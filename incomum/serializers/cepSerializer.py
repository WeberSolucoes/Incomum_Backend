import re
from rest_framework import serializers
from ..models.cep import Cep

class CepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cep
        fields = '__all__'
