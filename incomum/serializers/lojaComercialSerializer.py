from rest_framework import serializers
from ..models.lojaComercial import LojaComercial

class LojaComercialSerializer(serializers.ModelSerializer):
    class Meta:
        model = LojaComercial
        fields = '__all__'
class LojaComercialCreateSerializer(serializers.Serializer):
    loj_codigo = serializers.IntegerField(required=True)
    aco_codigo = serializers.IntegerField()