from rest_framework import serializers
from ..models.relatorio import Relatorio
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

class RelatorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relatorio
        fields = '__all__'
