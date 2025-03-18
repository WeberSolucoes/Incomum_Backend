import re
from rest_framework import serializers
from ..models.situacaoProtocolo import SituacaoProtocolo

class SituacaoProtocoloSerializer(serializers.ModelSerializer):
    class Meta:
        model = SituacaoProtocolo
        fields = '__all__'
