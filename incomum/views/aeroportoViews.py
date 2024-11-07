from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_yasg.utils import swagger_auto_schema
from ..serializers.aeroportoSerializer import AeroportoSerializer
from ..services import aeroportoService
from rest_framework.permissions import AllowAny


@swagger_auto_schema(
    methods=['post'],
    request_body=AeroportoSerializer,
    responses={200: AeroportoSerializer},
    tags=['Agencia']
)
@api_view(['POST'])
@permission_classes([AllowAny]) 
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create(request):
    return aeroportoService.create(request)

@swagger_auto_schema(
    methods=['get'],
    responses={200: AeroportoSerializer},
    tags=['Agencia']
)
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([AllowAny]) 
@permission_classes([IsAuthenticated])
def find_by_id(request,id):
    return aeroportoService.find_by_id(id)

@swagger_auto_schema(
    methods=['get'],
    responses={200: AeroportoSerializer(many=True)},
    tags=['Agencia']
)
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([AllowAny])
@permission_classes([IsAuthenticated])
def list_all(request):
    return aeroportoService.list_all()

@swagger_auto_schema(
    methods=['put'],
    request_body=AeroportoSerializer,
    responses={200: AeroportoSerializer},
    tags=['Agencia']
)
@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([AllowAny]) 
@permission_classes([IsAuthenticated])
def update(request, id):
    return aeroportoService.update(request, id)

@swagger_auto_schema(
    methods=['delete'],
    responses={200: AeroportoSerializer},
    tags=['Agencia']
)
@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([AllowAny]) 
@permission_classes([IsAuthenticated])
def delete(request, id):
    return aeroportoService.delete(id)
