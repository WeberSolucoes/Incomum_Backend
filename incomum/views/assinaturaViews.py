from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from ..serializers.assinaturaSerializer import *
from ..models import *
from ..services import assinaturaService

@swagger_auto_schema(
        methods=['get'], 
        responses={200: AssinaturaSerializer},
        tags=['Loja'])
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def find_by_id(request, id):
    return assinaturaService.findById(id)

@swagger_auto_schema(
        methods=['post'],
        request_body= AssinaturaSerializer,
        responses={201: AssinaturaSerializer},
        tags=['Loja'])
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create(request):
    return assinaturaService.create(request)

@swagger_auto_schema(
        methods=['get'],
        responses={200: AssinaturaSerializer(many=True)},
        tags=['Loja'])
@api_view(['GET'])
@authentication_classes([JWTAuthentication]) 
@permission_classes([IsAuthenticated])
def find_by_loja(request, id):
    return assinaturaService.findByLoja(id)

@swagger_auto_schema(
        methods=['put'],
        request_body=AssinaturaSerializer,
        responses={200: AssinaturaSerializer},
        tags=['Loja'])
@api_view(['PUT'])
@authentication_classes([JWTAuthentication]) 
@permission_classes([IsAuthenticated])
def update(request, id):
    return assinaturaService.update(request, id)

@swagger_auto_schema(
        methods=['delete'],
        responses={204: openapi.Response(description="No Content")},
        tags=['Loja'])
@api_view(['DELETE'])
@authentication_classes([JWTAuthentication]) 
@permission_classes([IsAuthenticated])
def delete(request, id):
    return assinaturaService.delete(id)

@swagger_auto_schema(
        methods=['get'],
        responses={200: AssinaturaSerializer(many=True)},
        tags=['Loja'])
@api_view(['GET'])

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def list_all(request):
    return assinaturaService.list_all()
