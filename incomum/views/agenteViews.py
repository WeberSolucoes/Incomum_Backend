from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_yasg.utils import swagger_auto_schema
from ..serializers.agenteSerializer import AgenteSerializer
from ..services import agenteService
from rest_framework.permissions import AllowAny


@swagger_auto_schema(
    methods=['post'],
    request_body=AgenteSerializer,
    responses={200: AgenteSerializer},
    tags=['Agencia']
)
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create(request):
    return agenteService.create(request)

@swagger_auto_schema(
    methods=['get'],
    responses={200: AgenteSerializer},
    tags=['Agencia']
)
@api_view(['GET'])
@authentication_classes([JWTAuthentication]) 
@permission_classes([IsAuthenticated])
def find_by_id(request,id):
    return agenteService.find_by_id(id)

@swagger_auto_schema(
    methods=['get'],
    responses={200: AgenteSerializer(many=True)},
    tags=['Agencia']
)
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def list_all(request):
    return agenteService.list_all()

@swagger_auto_schema(
    methods=['put'],
    request_body=AgenteSerializer,
    responses={200: AgenteSerializer},
    tags=['Agencia']
)
@api_view(['PUT'])
@authentication_classes([JWTAuthentication]) 
@permission_classes([IsAuthenticated])
def update(request, id):
    return agenteService.update(request, id)

@swagger_auto_schema(
    methods=['delete'],
    responses={200: AgenteSerializer},
    tags=['Agencia']
)
@api_view(['DELETE'])
@authentication_classes([JWTAuthentication]) 
@permission_classes([IsAuthenticated])
def delete(request, id):
    return agenteService.delete(id)


@swagger_auto_schema(
    methods=['get'],
    responses={200: AgenteSerializer},
    tags=['Agencia']
)
@api_view(['GET'])
@authentication_classes([JWTAuthentication]) 
@permission_classes([IsAuthenticated])
def get_agentes_por_agencia (request, age_codigo):
    return agenteService.get_agentes_por_agencia(request,age_codigo)
