from rest_framework import serializers
from ..models.banco import Banco

class BancoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banco
        fields = '__all__'
