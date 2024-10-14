from rest_framework import serializers
from ..models.relatorio import Relatorio
import locale

# Configurando a localização para 'pt_BR.UTF-8' (Brasil)
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

class RelatorioSerializer(serializers.ModelSerializer):
    # Campo customizado para valor formatado
    valor_formatado = serializers.SerializerMethodField()

    class Meta:
        model = Relatorio
        fields = '__all__'  # Ou pode listar os campos específicos, incluindo 'valor_formatado'

    # Método para formatar o valor usando a localização brasileira
    def get_valor_formatado(self, obj):
        # Supondo que o campo que você quer formatar é 'valor'
        if obj.valor:
            # Formata o valor como moeda brasileira (R$)
            return locale.currency(obj.valor, grouping=True)
        return None

