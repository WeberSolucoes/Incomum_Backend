import re
from rest_framework import serializers
from ..models.tipoRegime import TipoRegime

class TipoRegimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoRegime
        fields = '__all__'
