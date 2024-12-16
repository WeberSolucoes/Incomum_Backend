import re
from rest_framework import serializers
from ..models.despesas import Despesas

class DespesasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despesas
        fields = '__all__'
