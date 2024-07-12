from rest_framework import serializers
from django.contrib.auth.models import User
from ..models.modelExemplo import Tarefa


class MeuModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class myModelSaveDto(serializers.Serializer):
    nome = serializers.CharField(max_length=100)
    concluida = serializers.BooleanField(default=False)

class myModelUpdateDto(serializers.Serializer):
    nome = serializers.CharField(max_length=100, required=False)
    concluida = serializers.BooleanField(required=False)
    created = serializers.DateTimeField(required=False)