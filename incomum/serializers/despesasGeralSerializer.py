import re
from rest_framework import serializers
from ..models.despesasGeral import DespesasGeral

class DespesasGeralSerializer(serializers.ModelSerializer):
    class Meta:
        model = DespesasGeral
        fields = '__all__'
