from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_yasg.utils import swagger_auto_schema
from ..serializers.vendedorSerializer import VendedorSerializer
from ..services import vendedorService
from rest_framework.permissions import AllowAny

@swagger_auto_schema(
    methods=['post'],
    request_body=VendedorSerializer,
    responses={200: VendedorSerializer},
    tags=['Vendedor']
)
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([AllowAny])
@permission_classes([IsAuthenticated])
def create(request):
    return vendedorService.create(request)

@swagger_auto_schema(
    methods=['get'],
    responses={200: VendedorSerializer},
    tags=['Vendedor']
)
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([AllowAny])
@permission_classes([IsAuthenticated])
def find_by_id(request,id):
    return vendedorService.find_by_id(id)

@swagger_auto_schema(
    methods=['get'],
    responses={200: VendedorSerializer(many=True)},
    tags=['Vendedor']
)
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def list_all(request):
    return vendedorService.list_all()

@swagger_auto_schema(
    methods=['put'],
    request_body=VendedorSerializer,
    responses={200: VendedorSerializer},
    tags=['Vendedor']
)
@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([AllowAny])
@permission_classes([IsAuthenticated])
def update(request, id):
    return vendedorService.update(request, id)

@swagger_auto_schema(
    methods=['delete'],
    responses={200: VendedorSerializer},
    tags=['Vendedor']
)
@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([AllowAny])
@permission_classes([IsAuthenticated])
def delete(request, id):
    return vendedorService.delete(id)
