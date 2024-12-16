from rest_framework import serializers
from ..models.centroCusto import CentroCusto

class CentroCustoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentroCusto
        fields = '__all__'
