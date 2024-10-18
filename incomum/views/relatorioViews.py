from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from incomum.serializers.lojaSerializer import LojaSerializer

from ..serializers.relatorioSerializer import RelatorioSerializer
from ..models import *
from ..services import relatorioService
from rest_framework.permissions import AllowAny


@swagger_auto_schema(
        methods=['get'],
        tags=['Relatorio'])
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([AllowAny])
def list_all_byfilter(request):
    return relatorioService.list_all_byfilter(request)

@swagger_auto_schema(
        methods=['get'],
        tags=['Relatorio'])
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([AllowAny])
def total_byfilter(request):
    return relatorioService.total_byfilter(request)

@swagger_auto_schema(
        methods=['get'],
        tags=['Relatorio'])
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([AllowAny])
def list_all_lojas_byfilter(request):
    return relatorioService.list_all_lojas_byfilter(request)

@swagger_auto_schema(
        methods=['get'],
        tags=['Relatorio'])
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([AllowAny])
def list_all_areas_byfilter(request):
    return relatorioService.list_all_areas_byfilter(request)

@swagger_auto_schema(
        methods=['get'],
        tags=['Relatorio'])
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([AllowAny])
def list_all_vendedores_byfilter(request):
    return relatorioService.list_all_vendedores_byfilter(request)

@swagger_auto_schema(
        methods=['get'],
        tags=['Relatorio'])
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([AllowAny])
def list_all_agencias_byfilter(request):
    return relatorioService.list_all_agencias_byfilter(request)

@swagger_auto_schema(
        methods=['get'],
        tags=['Relatorio'])
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([AllowAny])
def list_all_areas(request, unidade_id=None):
    # Chama a função de serviço passando a unidade_id (ou None)
    return relatorioService.list_all_areas(request, unidade_id)

@swagger_auto_schema(
        methods=['get'],
        tags=['Relatorio'])
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([AllowAny])
def create_excel_byfilter(request):
    return relatorioService.create_excel_byfilter(request)
