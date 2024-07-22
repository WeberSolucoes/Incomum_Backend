from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated


from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from ..serializers.usuarioSerializer import *
from ..models import *
from ..services import usuarioService

@swagger_auto_schema(
    methods=['get'],
    responses={200: UsuarioDTOSerializer},
    tags=['Usuario']
)
@api_view(['GET'])
def findById(request, id):
    return usuarioService.findById(id)


@swagger_auto_schema(
    methods=['get'],
    responses={200: UsuarioDTOSerializer(many=True)},
    tags=['Usuario']
)
@api_view(['GET'])
def list_all(request):
    return usuarioService.list_all()


@swagger_auto_schema(
    methods=['post'],
    request_body=UsuarioDTOSerializer,
    responses={200: UsuarioDTOSerializer},
    tags=['Usuario']
)
@api_view(['POST'])
def create(request):
    return usuarioService.create(request)


@swagger_auto_schema(
    methods=['put'],
    request_body=UsuarioDTOSerializer,
    responses={200: UsuarioDTOSerializer},
    tags=['Usuario']
)
@api_view(['PUT'])
def update(request, id):
    return usuarioService.update(request, id)

@swagger_auto_schema(
    methods=['delete'],
    responses={204: openapi.Response(description="No Content")},
    tags=['Usuario']
)
@api_view(['DELETE'])
def delete(request, id):
    return usuarioService.delete(id)


@swagger_auto_schema(
    methods=['post'],
    request_body= EmailSerializer,
    responses={200: "Email enviado com sucesso"},
    tags=['Usuario']
)
@api_view(['POST'])
@permission_classes([AllowAny])
def update_password(request):
    return usuarioService.update_password(request)

@swagger_auto_schema(
    methods=['post'],
    request_body= PasswordSerializer,
    responses={200: "Senha Alterada com sucesso"},
    tags=['Usuario']
)
@api_view(['POST'])
@permission_classes([AllowAny])
def update_password_confirm(request, uidb64, token):
    return usuarioService.update_password_confirm(request, uidb64, token)

@swagger_auto_schema(
    methods=['get'],
    responses={200: UserGruposDTOSerializer(many=True)},
    tags=['Usuario']
)
@api_view(['GET'])
def list_groups(request, id):
    return usuarioService.list_grupos(id)

@swagger_auto_schema(
    methods=['post'],
    request_body= UserGruposUpdateDTOSerializer,
    responses={200: UserGruposDTOSerializer(many=True)},
    tags=['Usuario']
)
@api_view(['POST'])
def update_groups(request, id):
    return usuarioService.update_grupos(request, id)

@swagger_auto_schema(
    methods=['get'],
    responses={200: UserPermissionsDTOSerializer(many=True)},
    tags=['Usuario']
)
@api_view(['GET'])
def list_permissions(request, id):
    return usuarioService.list_permissions(id)

@swagger_auto_schema(
    methods=['post'],
    request_body= UserPermissionsUpdateDTOSerializer,
    responses={200: UserPermissionsDTOSerializer(many=True)},
    tags=['Usuario']
)
@api_view(['POST'])
def update_permissions(request, id):
    return usuarioService.update_permissions(request, id)