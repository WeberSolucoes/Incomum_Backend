# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import Permission, Group

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'

class PermissionResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    codename = serializers.CharField()

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class GroupResponseSerializer(serializers.Serializer):
    name = serializers.CharField()
    permissions = PermissionResponseSerializer(many=True)

class PermissionByGroupSerializer(serializers.Serializer):
    ids = serializers.ListField(child=serializers.IntegerField())
