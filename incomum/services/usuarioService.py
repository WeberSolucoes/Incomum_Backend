from rest_framework.response import Response
from rest_framework import status
from ..models.usuario import Usuario as User 
from ..serializers.usuarioSerializer import UsuarioDTOSerializer
from ..mappers.usuarioMapper import *
from django.db.utils import IntegrityError

def findById(id) -> Response:
    try:
        user: User = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = EntityToDto(user)
    return Response(serializer.data, status=status.HTTP_200_OK)

def list_all() -> Response:
    users = User.objects.all()
    serializer = EntitiesToDtos(users)
    return Response(serializer.data, status=status.HTTP_200_OK)

def create(request) -> Response:
    serializer = UsuarioDTOSerializer(data=request.data)
    if serializer.is_valid():
        user: Usuario = DtoToEntity(serializer)
        senha = user.first_name[0] + '@' + user.usr_cpf
        user.set_password(senha)
        try:
            user.save()
        except IntegrityError as e:
            return Response(status=status.HTTP_409_CONFLICT)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def update(request, id) -> Response:
    try:
        user: User = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UsuarioDTOSerializer(data=request.data)
    if serializer.is_valid():
        DtoToEntityUpdate(serializer, user)
        user.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def delete(id) -> Response:
    try:
        user: User = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)