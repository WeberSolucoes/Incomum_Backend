import re
from rest_framework import serializers
from ..models.pais import Pais

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = '__all__'
