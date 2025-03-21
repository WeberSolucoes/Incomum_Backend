from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_yasg.utils import swagger_auto_schema
from ..serializers.userSerializer import UserSerializer
from ..services import userService
from rest_framework.permissions import AllowAny

@swagger_auto_schema(
    methods=['post'],  # A requisição será via POST
    request_body=UserSerializer,  # Validação do corpo da requisição com o serializer
    responses={200: UserSerializer},  # A resposta segue o formato do serializer
    tags=['Usuario']  # Tag para documentação no Swagger
)
@api_view(['POST'])
@permission_classes([AllowAny])  # Permissão aberta para todos
def login(request):
    # Passa o request para o serviço de login
    return userService.login(request)

@swagger_auto_schema(
    methods=['get'],  # A requisição será via GET
    request_body=UserSerializer,  # Validação do corpo da requisição com o serializer
    responses={200: UserSerializer},  # A resposta segue o formato do serializer
    tags=['Usuario']  # Tag para documentação no Swagger
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])  # Permite apenas usuários autenticado
def user_permissions_view(request):
    # Passa o request para o serviço de login
    return userService.user_permissions_view(request)


@swagger_auto_schema(
    methods=['post'],  # A requisição será via GET
    request_body=UserSerializer,  # Validação do corpo da requisição com o serializer
    responses={200: UserSerializer},  # A resposta segue o formato do serializer
    tags=['Usuario']  # Tag para documentação no Swagger
)
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([AllowAny])
def PasswordRequest(request):
    # Passa o request para o serviço de login
    return userService.PasswordRequest(request)


@swagger_auto_schema(
    methods=['post'],  # A requisição será via GET
    request_body=UserSerializer,  # Validação do corpo da requisição com o serializer
    responses={200: UserSerializer},  # A resposta segue o formato do serializer
    tags=['Usuario']  # Tag para documentação no Swagger
)
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([AllowAny])
def PasswordReset(request, uid, token):
    # Passa o request para o serviço de login
    return userService.PasswordReset(request, uid, token)


@swagger_auto_schema(
    methods=['get'],  # A requisição será via GET
    request_body=UserSerializer,  # Validação do corpo da requisição com o serializer
    responses={200: UserSerializer},  # A resposta segue o formato do serializer
    tags=['Usuario']  # Tag para documentação no Swagger
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])  # Permite apenas usuários autenticado
def get_user_id(request):
    # Passa o request para o serviço de login
    return userService.get_user_id(request)
