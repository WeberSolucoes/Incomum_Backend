from ..models.user import AuthUser
from rest_framework import serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = '__all__'
