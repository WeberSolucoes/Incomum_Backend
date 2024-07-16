# views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from ..serializers.tokenSerializer import loginSerializer, registerSerializer
from django.contrib.auth.models import User
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(
    method='post',
    request_body=loginSerializer,
    responses={200: 'Token gerado com sucesso'},
)
@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    serializer = loginSerializer(data=request.data)

    if serializer.is_valid():
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='post',
    request_body=registerSerializer,
    responses={201: 'Usuario Criado'},
)
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = registerSerializer(data=request.data)
    if serializer.is_valid():
        entity: User = User()
        entity.username = serializer.validated_data.get('username')
        entity.email = serializer.validated_data.get('email')
        entity.set_password(serializer.validated_data.get('password'))
        entity.save()
        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
