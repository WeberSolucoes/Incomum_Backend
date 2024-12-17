from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from ..serializers.areaComercialSerializer import *
from ..models import *
from ..services import areaComercialService

@swagger_auto_schema(
        methods=['get'], 
        responses={200: AreaComercialSerializer},
        tags=['AreaComercial'])
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def find_by_id(request, id):
    return areaComercialService.findById(id)

@swagger_auto_schema(
        methods=['post'],
        request_body=AreaComercialCreateSerializer,
        responses={201: AreaComercialSerializer},
        tags=['AreaComercial'])
@api_view(['POST'])
@authentication_classes([JWTAuthentication]) 
@permission_classes([IsAuthenticated])
def create(request):
    return areaComercialService.create(request)

@swagger_auto_schema(
        methods=['get'],
        responses={200: AreaComercialSerializer(many=True)},
        tags=['AreaComercial'])
@api_view(['GET'])
@authentication_classes([JWTAuthentication]) 
@permission_classes([IsAuthenticated])
def find_by_loja(request, id):
    return areaComercialService.findByLoja(id)

@swagger_auto_schema(
        methods=['put'],
        request_body=AreaComercialCreateSerializer,
        responses={200: AreaComercialSerializer},
        tags=['AreaComercial'])
@api_view(['PUT'])
@authentication_classes([JWTAuthentication]) 
@permission_classes([IsAuthenticated])
def update(request, id):
    return areaComercialService.update(request, id)

@swagger_auto_schema(
        methods=['delete'],
        responses={204: openapi.Response(description="No Content")},
        tags=['AreaComercial'])
@api_view(['DELETE'])
@authentication_classes([JWTAuthentication]) 
@permission_classes([IsAuthenticated])
def delete(request, id):
    return areaComercialService.delete(id)

@swagger_auto_schema(
        methods=['get'],
        responses={200: AreaComercialSerializer(many=True)},
        tags=['AreaComercial'])
@api_view(['GET'])
@authentication_classes([JWTAuthentication]) 
@permission_classes([IsAuthenticated])
def list_all(request):
    return areaComercialService.list_all()
