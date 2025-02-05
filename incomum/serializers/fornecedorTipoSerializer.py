import re
from rest_framework import serializers
from ..models.fornecedorTipo import FornecedorTipo

class FornecedorTipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FornecedorTipo
        fields = '__all__'
