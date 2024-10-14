from rest_framework import serializers
from ..models.relatorio import Relatorio
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

class RelatorioSerializer(serializers.ModelSerializer):
    valor_formatado = serializers.SerializerMethodField()

    class Meta:
        model = Relatorio
        fields = '__all__'  # Ou pode listar os campos específicos, incluindo 'valor_formatado'

    def get_valor_formatado(self, obj):
        return locale.currency(obj.valor, grouping=True)
