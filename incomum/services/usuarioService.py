from rest_framework.response import Response
from rest_framework import status
from ..models.usuario import Usuario as User 
from ..serializers.usuarioSerializer import UsuarioDTOSerializer

def findById(id) -> Response:
    try:
        user: User = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UsuarioDTOSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)

def list_all() -> Response:
    users = User.objects.all()
    serializer = UsuarioDTOSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

def create(request) -> Response:
    serializer = UsuarioDTOSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def update(request, id) -> Response:
    try:
        user: User = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UsuarioDTOSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def delete(id) -> Response:
    try:
        user: User = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)