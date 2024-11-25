from rest_framework import serializers
from ..models.bandeira import Bandeira

class BandeiraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bandeira
        fields = '__all__'
