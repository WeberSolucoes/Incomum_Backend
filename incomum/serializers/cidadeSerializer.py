import re
from rest_framework import serializers
from ..models.cidade import Cidade

class CidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cidade
        fields = '__all__'
