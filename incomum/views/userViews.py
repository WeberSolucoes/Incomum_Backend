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
@authentication_classes([JWTAuthentication])  # Usando JWT como autenticação
def login(request):
    # Passa o request para o serviço de login
    return userService.login(request)
