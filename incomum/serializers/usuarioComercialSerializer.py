from rest_framework import serializers
from ..models.usuario_areaComercial import UsuarioAreaComercial
from .areaComercialSerializer import AreaComercialSerializer

class UsuarioAreaComercialSerializer(serializers.ModelSerializer):
    loja_codigo = serializers.IntegerField(source='area_comercial.loja_codigo.loj_codigo', read_only=True)
    loja_descricao = serializers.CharField(source='area_comercial.loja_codigo.loj_descricao', read_only=True)

    class Meta:
        model = UsuarioAreaComercial
        fields = ['loja_codigo', 'loja_descricao']

class UsuarioAreaComercialCreateSerializer(serializers.Serializer):
    usuario_id = serializers.CharField(max_length=50)
    area_comercial_id = serializers.CharField(max_length=50)
