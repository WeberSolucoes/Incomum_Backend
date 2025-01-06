from rest_framework import serializers
from ..models.relatorio import Relatorio
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

class RelatorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relatorio
        fields = ['tur_codigo', 'fim_data', 'fim_tipo', 'tur_numerovenda','fim_valorliquido','fim_markup','fim_valorinc','fim_valorincajustado','aco_descricao','ven_descricao','age_descricao','fat_valorvendabruta']  # Exemplo de campos selecionados

