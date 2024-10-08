from rest_framework import serializers
from ..models.relatorio import Relatorio
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

class RelatorioSerializer(serializers.Serializer):
    aco_codigo = serializers.IntegerField(required=False, allow_null=True)
    fim_codigo = serializers.IntegerField(required=False, allow_null=True)
    fim_data = serializers.DateField()
    fim_markup = serializers.FloatField()
    fim_tipo = serializers.CharField()
    fim_valorinc = serializers.FloatField()
    fim_valorincajustado = serializers.FloatField()
    fim_valorliquido = serializers.FloatField()
    tur_codigo = serializers.IntegerField()
    tur_numerovenda = serializers.CharField()
