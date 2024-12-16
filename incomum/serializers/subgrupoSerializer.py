import re
from rest_framework import serializers
from ..models.subgrupo import Subgrupo

class SubgrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subgrupo
        fields = '__all__'
