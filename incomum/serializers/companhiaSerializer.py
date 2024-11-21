import re
from rest_framework import serializers
from ..models.companhia import Companhia

class CompanhiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Companhia
        fields = '__all__'
