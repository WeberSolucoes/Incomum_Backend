import re
from rest_framework import serializers
from ..models.departamento import Departamento

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'
