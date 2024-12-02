import re
from rest_framework import serializers
from ..models.parceiro import Parceiro

class ParceiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parceiro
        fields = '__all__'
