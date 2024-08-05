from rest_framework import serializers
from ..models.areaComercial import AreaComercial
class AreaComercialSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaComercial
        fields = '__all__'
class AreaComercialCreateSerializer(serializers.Serializer):
    aco_descricao = serializers.CharField(max_length=50)
    aco_situacao = serializers.IntegerField()
    aco_rateio = serializers.IntegerField()
    id_loja = serializers.IntegerField()
