import re
from rest_framework import serializers
from ..models.loja import Loja

class LojaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loja
        fields = '__all__'

    def validate(self, data):
        # Validação e conversão do CEP
        cep = data.get('cep_codigo', '')
        cep_str = str(cep).replace('-', '')
        if not self.is_valid_cep(cep_str):
            raise serializers.ValidationError({"cep_codigo": "CEP inválido"})
        data['cep_codigo'] = int(cep_str)
        
        # Validação do CNPJ
        cnpj = data.get('loj_cnpj', '')
        if not self.is_valid_cnpj(cnpj):
            raise serializers.ValidationError({'loj_cnpj': 'O CNPJ deve estar no formato 00.000.000/0000-00.'})

        return data

    def is_valid_cep(self, cep):
        if not cep.isdigit() or len(cep) != 8:
            return False
        return True
    def is_valid_cnpj(self, cnpj):
        # Remove qualquer caractere não numérico do CNPJ
        cnpj = re.sub(r'\D', '', cnpj)
        # Verifica se o CNPJ tem 14 dígitos
        if len(cnpj) != 14:
            return False
        # Verifica o formato com regex
        return bool(re.match(r'^\d{14}$', cnpj))