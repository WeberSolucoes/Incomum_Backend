import re
from rest_framework import serializers
from ..models.protocolo import Protocolo

class ProtocoloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Protocolo
        fields = '__all__'
