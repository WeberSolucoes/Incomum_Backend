from rest_framework import serializers
from ..models.relatorio import Relatorio
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

class RelatorioSerializer(serializers.ModelSerializer):
    nome_loja = serializers.SerializerMethodField()
    aco_descricao = serializers.SerializerMethodField()
    fim_data = serializers.SerializerMethodField()
    fim_valorliquido = serializers.SerializerMethodField()
    fim_markup = serializers.SerializerMethodField()
    fim_valorinc = serializers.SerializerMethodField()
    fim_valorincajustado = serializers.SerializerMethodField()

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
    
    def get_fim_data(self, obj):
        return obj.fim_data.strftime('%d/%m/%Y') if obj.fim_data else None

    def get_fim_valorliquido(self, obj):
        return locale.currency(obj.fim_valorliquido, grouping=True, symbol=False) if obj.fim_valorliquido else None

    def get_fim_markup(self, obj):
        return locale.currency(obj.fim_markup, grouping=True, symbol=False) if obj.fim_markup else None

    def get_fim_valorinc(self, obj):
        return locale.currency(obj.fim_valorinc, grouping=True, symbol=False) if obj.fim_valorinc else None

    def get_fim_valorincajustado(self, obj):
        return locale.currency(obj.fim_valorincajustado, grouping=True, symbol=False) if obj.fim_valorincajustado else None
