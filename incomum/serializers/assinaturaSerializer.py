import re
from rest_framework import serializers
from ..models.assinatura import Assinatura

class AssinaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assinatura
        fields = '__all__'
