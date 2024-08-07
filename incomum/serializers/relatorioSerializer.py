from rest_framework import serializers

from ..models.relatorio import Relatorio

class RelatorioSerializer(serializers.ModelSerializer):
    nome_loja = serializers.SerializerMethodField()
    aco_descricao = serializers.SerializerMethodField()

    class Meta:
        model = Relatorio
        fields = [
            'fim_codigo',
            'tur_codigo',
            'loj_codigo',
            'fim_data',
            'aco_codigo',
            'fim_tipo',
            'tur_numerovenda',
            'fim_valorliquido',
            'fim_markup',
            'fim_valorinc',
            'fim_valorincajustado',
            'nome_loja',
            'aco_descricao'
        ]

    def get_nome_loja(self, obj):
        return obj.loj_codigo.loj_descricao if obj.loj_codigo else None
    def get_aco_descricao(self, obj):
        return obj.aco_codigo.aco_descricao if obj.aco_codigo else None