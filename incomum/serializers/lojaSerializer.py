import re
from rest_framework import serializers
from ..models.loja import Loja

class LojaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loja
        fields = '__all__'
