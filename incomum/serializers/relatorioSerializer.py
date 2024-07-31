from rest_framework import serializers

class RelatorioFiltersSerializer (serializers.Serializer):
    dataInicio = serializers.DateField(required=True)
    dataFim = serializers.DateField(required=True)
    loja = serializers.IntegerField(required=False)
    areaComercial = serializers.IntegerField(required=False)
    agencia = serializers.IntegerField(required=False)
    vendedor = serializers.IntegerField(required=False)

class RelatorioSimplificadoResponse (serializers.Serializer):
    id = serializers.IntegerField(required=True)
    tipo = serializers.CharField(required=True)
    numeroVenda = serializers.CharField(required=True)
    numeroPacote = serializers.IntegerField(required=False)
    dataVenda = serializers.CharField(required=True)
    valorLiquidoVenda = serializers.FloatField(required=True)
    markUp = serializers.FloatField(required=True)
    valorInc = serializers.FloatField(required=True)
    valorIncAjustado = serializers.FloatField(required=True)
    areaComercial = serializers.CharField(required=True)
    agencia = serializers.CharField(required=True)