from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from ..serializers.cidadeSerializer import *
from ..models import *
from ..services import cidadeService

@swagger_auto_schema(
        methods=['get'], 
        responses={200: CidadeSerializer},
        tags=['Loja'])
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def find_by_id(request, id):
    return cidadeService.findById(id)

@swagger_auto_schema(
        methods=['post'],
        request_body=CidadeSerializer,
        responses={201: CidadeSerializer},
        tags=['Loja'])
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create(request):
    return cidadeService.create(request)

@swagger_auto_schema(
        methods=['get'],
        responses={200: CidadeSerializer(many=True)},
        tags=['Loja'])
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def find_by_loja(request, id):
    return cidadeService.findByLoja(id)

@swagger_auto_schema(
        methods=['put'],
        request_body=CidadeSerializer,
        responses={200: CidadeSerializer},
        tags=['Loja'])
@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update(request, id):
    return cidadeService.update(request, id)

@swagger_auto_schema(
        methods=['delete'],
        responses={204: openapi.Response(description="No Content")},
        tags=['Loja'])
@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete(request, id):
    return cidadeService.delete(id)

@swagger_auto_schema(
        methods=['get'],
        responses={200: CidadeSerializer(many=True)},
        tags=['Loja'])
@api_view(['GET'])

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def list_all(request):
    return cidadeService.list_all()


@swagger_auto_schema(
        methods=['get'],
        responses={200: CidadeSerializer(many=True)},
        tags=['Loja'])
@api_view(['GET'])

@authentication_classes([JWTAuthentication])
@permission_classes([AllowAny])
@permission_classes([IsAuthenticated])
def search_cidades(request):
    return cidadeService.search_cidades(request)

