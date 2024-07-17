from ..models.usuario import *
from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class UsuarioDTOSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    dep_id = serializers.ListField(child=serializers.IntegerField())
    funcoes_id = serializers.ListField(child=serializers.IntegerField())
    ven_cod = serializers.IntegerField()
    cpf = serializers.CharField()
    data_nasc = serializers.DateField()
    loja_id = serializers.IntegerField()