from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_yasg.utils import swagger_auto_schema
from ..serializers.agenciaBancariaSerializer import AgenciaBancariaSerializer
from ..services import agenciaBancariaService

@swagger_auto_schema(
    methods=['post'],
    request_body=AgenciaBancariaSerializer,
    responses={200: AgenciaBancariaSerializer},
    tags=['Agencia Bancária']
)
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create(request):
    return agenciaBancariaService.create(request)

@swagger_auto_schema(
    methods=['get'],
    responses={200: AgenciaBancariaSerializer},
    tags=['Agencia Bancária']
)
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def find_by_id(request, id):
    return agenciaBancariaService.find_by_id(id)

@swagger_auto_schema(
    methods=['get'],
    responses={200: AgenciaBancariaSerializer(many=True)},
    tags=['Agencia Bancária']
)
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def list_all(request):
    return agenciaBancariaService.list_all()

@swagger_auto_schema(
    methods=['put'],
    request_body=AgenciaBancariaSerializer,
    responses={200: AgenciaBancariaSerializer},
    tags=['Agencia Bancária']
)
@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update(request, id):
    return agenciaBancariaService.update(request, id)

@swagger_auto_schema(
    methods=['delete'],
    responses={200: "Agência Bancária deletada com sucesso"},
    tags=['Agencia Bancária']
)
@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete(request, id):
    return agenciaBancariaService.delete(id)
