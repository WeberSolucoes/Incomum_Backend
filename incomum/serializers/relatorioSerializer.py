from rest_framework import serializers
from ..models.relatorio import Relatorio

class RelatorioSerializer(serializers.ModelSerializer):
    # Campo customizado para valor formatado
    valor_formatado = serializers.FloatField(source='valor', read_only=True)

    class Meta:
        model = Relatorio
        fields = '__all__'  # Ou pode listar os campos específicos

