from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from ..serializers.despesasGeralSerializer import *
from ..models import *
from ..services import despesasGeralService

@swagger_auto_schema(
        methods=['get'], 
        responses={200: DespesasGeralSerializer},
        tags=['Loja'])
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def find_by_id(request, id):
    return despesasGeralService.findById(id)

@swagger_auto_schema(
        methods=['post'],
        request_body=DespesasGeralSerializer,
        responses={201: DespesasGeralSerializer},
        tags=['Loja'])
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create(request):
    return despesasGeralService.create(request)

@swagger_auto_schema(
        methods=['get'],
        responses={200: DespesasGeralSerializer(many=True)},
        tags=['Loja'])
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def find_by_loja(request, id):
    return despesasGeralService.findByLoja(id)

@swagger_auto_schema(
        methods=['put'],
        request_body=DespesasGeralSerializer,
        responses={200: DespesasGeralSerializer},
        tags=['Loja'])
@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update(request, id):
    return despesasGeralService.update(request, id)

@swagger_auto_schema(
        methods=['delete'],
        responses={204: openapi.Response(description="No Content")},
        tags=['Loja'])
@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete(request, id):
    return despesasGeralService.delete(id)

@swagger_auto_schema(
        methods=['get'],
        responses={200: DespesasGeralSerializer(many=True)},
        tags=['Loja'])
@api_view(['GET'])

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def list_all(request):
    return despesasGeralService.list_all()
