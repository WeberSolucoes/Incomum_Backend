from rest_framework.decorators import api_view

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

