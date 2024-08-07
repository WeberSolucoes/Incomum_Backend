from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from ..serializers.usuarioComercialSerializer import *
from ..models import *
from ..services import usuarioComercialService

@swagger_auto_schema(
        methods=['get'], 
        responses={200: UsuarioAreaComercialSerializer},
        tags=['usr_comercial'])
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def find_by_id(request, id):
    return usuarioComercialService.findById(id)

@swagger_auto_schema(
        methods=['post'],
        request_body=UsuarioAreaComercialSerializer,
        responses={201: UsuarioAreaComercialSerializer},
        tags=['usr_comercial'])
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create(request):
    return usuarioComercialService.create(request)

@swagger_auto_schema(
        methods=['get'],
        responses={200: UsuarioAreaComercialSerializer(many=True)},
        tags=['usr_comercial'])
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def find_by_loja(request, id):
    return usuarioComercialService.findByLoja(id)

@swagger_auto_schema(
        methods=['put'],
        request_body=UsuarioAreaComercialSerializer,
        responses={200: UsuarioAreaComercialSerializer},
        tags=['usr_comercial'])
@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update(request, id):
    return usuarioComercialService.update(request, id)

@swagger_auto_schema(
        methods=['delete'],
        responses={204: openapi.Response(description="No Content")},
        tags=['usr_comercial'])
@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete(request, id):
    return usuarioComercialService.delete(id)

@swagger_auto_schema(
        methods=['get'],
        responses={200: UsuarioAreaComercialSerializer(many=True)},
        tags=['usr_comercial'])
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def list_all(request,id):
    return usuarioComercialService.list_all(request,id)