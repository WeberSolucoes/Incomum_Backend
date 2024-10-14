from rest_framework import serializers
from ..models.relatorio import Relatorio
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

class RelatorioSerializer(serializers.ModelSerializer):
    # Campo customizado para valor formatado
    valor_formatado = serializers.FloatField(source='valor', read_only=True)

    class Meta:
        model = Relatorio
        fields = '__all__'  # Ou pode listar os campos específicos

