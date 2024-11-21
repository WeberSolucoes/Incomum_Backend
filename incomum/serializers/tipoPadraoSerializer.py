import re
from rest_framework import serializers
from ..models.tipoPadrao import TipoPadrao

class TipoPadraoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPadrao
        fields = '__all__'
