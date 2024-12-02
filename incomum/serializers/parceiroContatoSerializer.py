import re
from rest_framework import serializers
from ..models.parceiroContato import ParceiroContato

class ParceiroContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParceiroContato
        fields = '__all__'
