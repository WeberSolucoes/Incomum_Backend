from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from ..serializers.lojaComercialSerializer import *
from ..models import *
from ..services import lojaComercialService

@swagger_auto_schema(
        methods=['get'], 
        responses={200: LojaComercialSerializer},
        tags=['LojaComercial'])
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def find_by_id(request, id):
    return lojaComercialService.findById(id)

@swagger_auto_schema(
        methods=['post'],
        request_body=LojaComercialCreateSerializer,
        responses={201: LojaComercialSerializer},
        tags=['AreaComercial'])
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create(request):
    return lojaComercialService.create(request)

@swagger_auto_schema(
        methods=['get'],
        responses={200: LojaComercialSerializer(many=True)},
        tags=['AreaComercial'])
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def find_by_loja(request, id):
    return lojaComercialService.findByLoja(id)

@swagger_auto_schema(
        methods=['put'],
        request_body=LojaComercialCreateSerializer,
        responses={200: LojaComercialSerializer},
        tags=['AreaComercial'])
@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update(request, id):
    return lojaComercialService.update(request, id)

@swagger_auto_schema(
        methods=['delete'],
        responses={204: openapi.Response(description="No Content")},
        tags=['AreaComercial'])
@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete(request, id):
    return lojaComercialService.delete(id)

@swagger_auto_schema(
        methods=['get'],
        responses={200: LojaComercialSerializer(many=True)},
        tags=['AreaComercial'])
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def list_all(request):
    return lojaComercialService.list_all()
