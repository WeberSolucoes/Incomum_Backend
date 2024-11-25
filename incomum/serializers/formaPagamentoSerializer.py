import re
from rest_framework import serializers
from ..models.formaPagamento import FormaPagamento

class FormaPagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormaPagamento
        fields = '__all__'
