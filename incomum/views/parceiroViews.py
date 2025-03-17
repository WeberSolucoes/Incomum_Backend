from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from ..serializers.parceiroSerializer import *
from ..models import *
from ..services import parceiroService

@swagger_auto_schema(
        methods=['get'], 
        responses={200: ParceiroSerializer},
        tags=['Loja'])
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def find_by_id(request, id):
    return parceiroService.findById(id)

@swagger_auto_schema(
        methods=['post'],
        request_body=ParceiroSerializer,
        responses={201: ParceiroSerializer},
        tags=['Loja'])
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create(request):
    return parceiroService.create(request)

@swagger_auto_schema(
        methods=['get'],
        responses={200: ParceiroSerializer(many=True)},
        tags=['Loja'])
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def find_by_loja(request, id):
    return parceiroService.findByLoja(id)

@swagger_auto_schema(
        methods=['put'],
        request_body=ParceiroSerializer,
        responses={200: ParceiroSerializer},
        tags=['Loja'])
@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update(request, id):
    return parceiroService.update(request, id)

@swagger_auto_schema(
        methods=['delete'],
        responses={204: openapi.Response(description="No Content")},
        tags=['Loja'])
@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete(request, id):
    return parceiroService.delete(id)

@swagger_auto_schema(
        methods=['get'],
        responses={200: ParceiroSerializer(many=True)},
        tags=['Loja'])
@api_view(['GET'])

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def list_all(request):
    return parceiroService.list_all()


@swagger_auto_schema(
        methods=['get'],
        responses={200: ParceiroSerializer(many=True)},
        tags=['Loja'])
@api_view(['GET'])

@authentication_classes([JWTAuthentication])
@permission_classes([AllowAny])
@permission_classes([IsAuthenticated])
def search(request):
    return parceiroService.search(request)
