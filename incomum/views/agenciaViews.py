from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_yasg.utils import swagger_auto_schema
from ..serializers.agenciaSerializer import AgenciaSerializer
from ..services import agenciaService
from rest_framework.permissions import AllowAny


@swagger_auto_schema(
    methods=['post'],
    request_body=AgenciaSerializer,
    responses={200: AgenciaSerializer},
    tags=['Agencia']
)
@api_view(['POST']) 
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create(request):
    return agenciaService.create(request)

@swagger_auto_schema(
    methods=['get'],
    responses={200: AgenciaSerializer},
    tags=['Agencia']
)
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def find_by_id(request,id):
    return agenciaService.find_by_id(id)

@swagger_auto_schema(
    methods=['get'],
    responses={200: AgenciaSerializer(many=True)},
    tags=['Agencia']
)
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def list_all(request):
    return agenciaService.list_all()

@swagger_auto_schema(
    methods=['put'],
    request_body=AgenciaSerializer,
    responses={200: AgenciaSerializer},
    tags=['Agencia']
)
@api_view(['PUT'])
@authentication_classes([JWTAuthentication]) 
@permission_classes([IsAuthenticated])
def update(request, id):
    return agenciaService.update(request, id)

@swagger_auto_schema(
    methods=['delete'],
    responses={200: AgenciaSerializer},
    tags=['Agencia']
)
@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete(request, id):
    return agenciaService.delete(id)


@swagger_auto_schema(
    methods=['post'],
    responses={200: AgenciaSerializer},
    tags=['Agencia']
)
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_logo(request, id):
    return agenciaService.update_logo(request, id)


@swagger_auto_schema(
    methods=['get'],
    responses={200: AgenciaSerializer},
    tags=['Agencia']
)
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_agencia_imagem(request, id):
    return agenciaService.get_agencia_imagem(request, id)
