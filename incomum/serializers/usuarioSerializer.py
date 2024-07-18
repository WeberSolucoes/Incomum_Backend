from ..models.usuario import *
from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class UsuarioDTOSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    first_name = serializers.CharField(required=False, allow_blank=True)
    last_name = serializers.CharField(required=False, allow_blank=True)
    dep_principal = serializers.IntegerField(required=False, allow_null=True)
    dep_id = serializers.ListField(child=serializers.IntegerField(),required=False)
    funcoes_id = serializers.ListField(child=serializers.IntegerField(),required=False)
    ven_cod = serializers.IntegerField(required=False, allow_null=True)
    cpf = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    data_nasc = serializers.DateField(required=False, allow_null=True)
    loja_id = serializers.IntegerField(required=False, allow_null=True)