import re
from rest_framework import serializers
from ..models.duplicata import Duplicata

class DuplicataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Duplicata
        fields = '__all__'
