from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from ..serializers.lojaSerializer import *
from ..models import *
from ..services import lojaService

@swagger_auto_schema(
        methods=['get'], 
        responses={200: LojaSerializer},
        tags=['Loja'])
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def find_by_id(request, id):
    return lojaService.findById(id)

@swagger_auto_schema(
        methods=['post'],
        request_body=LojaSerializer,
        responses={201: LojaSerializer},
        tags=['Loja'])
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create(request):
    return lojaService.create(request)

@swagger_auto_schema(
        methods=['get'],
        responses={200: LojaSerializer(many=True)},
        tags=['Loja'])
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def find_by_loja(request, id):
    return lojaService.findByLoja(id)

@swagger_auto_schema(
        methods=['put'],
        request_body=LojaSerializer,
        responses={200: LojaSerializer},
        tags=['Loja'])
@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update(request, id):
    return lojaService.update(request, id)

@swagger_auto_schema(
        methods=['delete'],
        responses={204: openapi.Response(description="No Content")},
        tags=['Loja'])
@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete(request, id):
    return lojaService.delete(id)

@swagger_auto_schema(
        methods=['get'],
        responses={200: LojaSerializer(many=True)},
        tags=['Loja'])
@api_view(['GET'])

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def list_all(request):
    return lojaService.list_all()



@swagger_auto_schema(
    methods=['get'],
    responses={200: LojaSerializer(many=True)},
    tags=['Loja']
)
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def find_vinculadas(request, aco_codigo):
    lojas_vinculadas = lojaService.find_vinculadas(aco_codigo)
    return Response(LojaSerializer(lojas_vinculadas, many=True).data)
