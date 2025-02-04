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
@permission_classes([IsAuthenticated])
def list_all_byfilter(request):
    return relatorioService.list_all_byfilter(request)

@swagger_auto_schema(
        methods=['get'],
        tags=['Relatorio'])
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def total_byfilter(request):
    return relatorioService.total_byfilter(request)

@swagger_auto_schema(
        methods=['get'],
        tags=['Relatorio'])
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def list_all_lojas_byfilter(request):
    return relatorioService.list_all_lojas_byfilter(request)

@swagger_auto_schema(
        methods=['get'],
        tags=['Relatorio'])
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def list_all_areas_byfilter(request):
    return relatorioService.list_all_areas_byfilter(request)

@swagger_auto_schema(
        methods=['get'],
        tags=['Relatorio'])
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def list_all_vendedores_byfilter(request):
    return relatorioService.list_all_vendedores_byfilter(request)

@swagger_auto_schema(
        methods=['get'],
        tags=['Relatorio'])
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def list_all_agencias_byfilter(request):
    return relatorioService.list_all_agencias_byfilter(request)

@swagger_auto_schema(
        methods=['get'],
        tags=['Relatorio'])
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def list_all_areas(request, unidade_id=None):
    # Chama a função de serviço passando a unidade_id (ou None)
    return relatorioService.list_all_areas(request, unidade_id)

@swagger_auto_schema(
    methods=['get'],
    tags=['Relatorio'])
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create_excel_byfilter(request):
    print(f"Headers: {request.headers}")  # Log para verificar cabeçalhos
    return relatorioService.create_excel_byfilter(request)

@swagger_auto_schema(
        methods=['get'],
        tags=['Relatorio'])
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def list_all_area(request):
    return relatorioService.list_all_area(request)


@swagger_auto_schema(
        methods=['get'],
        tags=['Relatorio'])
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([AllowAny])
def obter_dados_unidade(request):
    return relatorioService.obter_dados_unidade(request)

@swagger_auto_schema(
        methods=['get'],
        tags=['Relatorio'])
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([AllowAny])
def obter_dados_agencia(request):
    return relatorioService.obter_dados_agencia(request)


@swagger_auto_schema(
        methods=['post'],
        tags=['Relatorio'])
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([AllowAny])
def obter_dados_area_comercial(request):
    return relatorioService.obter_dados_area_comercial(request)


@swagger_auto_schema(
        methods=['get'],
        tags=['Relatorio'])
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([AllowAny])
def exportar_dados_agencia_para_excel(request):
    return relatorioService.exportar_dados_agencia_para_excel(request)



@swagger_auto_schema(
        methods=['get'],
        tags=['Relatorio'])
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([AllowAny])
def exportar_dados_loja_para_excel(request):
    return relatorioService.exportar_dados_loja_para_excel(request)


@swagger_auto_schema(
        methods=['get'],
        tags=['Relatorio'])
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([AllowAny])
def exportar_area_comercial_para_excel(request):
    return relatorioService.exportar_area_comercial_para_excel(request)

