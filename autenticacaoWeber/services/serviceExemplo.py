from rest_framework.request import Request
from rest_framework.response import Response
from django.contrib.auth.models import User
from ..serializers.serializerExemplo import UserSerializer
from rest_framework import status

def userDetailsService(request:Request) -> Response:
    id = request.user.id
    entity: User = User.objects.get(id=id)
    if not entity.is_active:
        raise User.DoesNotExist("Usuário Inativo")
    response = UserSerializer(entity)
    return Response(response.data, status=status.HTTP_200_OK)