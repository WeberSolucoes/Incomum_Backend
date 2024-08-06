from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from ..serializers.relatorioSerializer import *
from ..models import *
from ..services import relatorioService

@swagger_auto_schema(
        methods=['get'], 
        responses={200: relatorioSerializer},
        tags=['Relatorio'])
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def find_by_id(request, id):
    return relatorioService.findById(id)

@swagger_auto_schema(
        methods=['post'],
        request_body=relatorioSerializer,
        responses={201: relatorioSerializer},
        tags=['Relatorio'])
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create(request):
    return relatorioService.create(request)

@swagger_auto_schema(
        methods=['get'],
        responses={200: relatorioSerializer(many=True)},
        tags=['Relatorio'])
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def find_by_loja(request, id):
    return relatorioService.findByLoja(id)

@swagger_auto_schema(
        methods=['put'],
        request_body=relatorioSerializer,
        responses={200: relatorioSerializer},
        tags=['Relatorio'])
@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update(request, id):
    return relatorioService.update(request, id)

@swagger_auto_schema(
        methods=['delete'],
        responses={204: openapi.Response(description="No Content")},
        tags=['Relatorio'])
@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete(request, id):
    return relatorioService.delete(id)

@swagger_auto_schema(
        methods=['get'],
        responses={200: relatorioSerializer(many=True)},
        tags=['Relatorio'])
@api_view(['GET'])
def list_all(request):
    return relatorioService.list_all(request)

@swagger_auto_schema(
        methods=['get'],
        responses={200: relatorioSerializer(many=True)},
        tags=['Relatorio'])
@api_view(['GET'])
def filtraunidade(request):
    return relatorioService.filtraunidade(request)