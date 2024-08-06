from rest_framework.response import Response
from rest_framework import status
from ..models import *
from ..serializers.usuarioComercialSerializer import *

def findById(id) -> Response:
    try:
        usr_comercial: UsuarioAreaComercial = UsuarioAreaComercial.objects.get(usuario = id)
    except UsuarioAreaComercial.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UsuarioAreaComercialSerializer(usr_comercial)
    return Response(serializer.data)

def create(request) -> Response:
    serializer = UsuarioAreaComercialCreateSerializer(data=request.data)
    if serializer.is_valid():
        try:
            area: UsuarioAreaComercial = UsuarioAreaComercial()
            area.usuario_id = serializer.validated_data['usuario_id']
            area.area_comercial_id = serializer.validated_data['area_comercial_id']
            area.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Loja.DoesNotExist:
            return Response({'message': 'Loja não encontrada.'},status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
def update(request, id) -> Response:
    try:
        usr_comercial: UsuarioAreaComercial = UsuarioAreaComercial.objects.get(usuario = id)
    except UsuarioAreaComercial.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UsuarioAreaComercialSerializer(usr_comercial, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def delete(id) -> Response:
    try:
        usr_comercial: UsuarioAreaComercial = UsuarioAreaComercial.objects.get(usuario = id)
    except UsuarioAreaComercial.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    usr_comercial.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

def list_all(request, id) -> Response:
    # Verificar se o ID é negativo ou zero
    if id <= 0:
        return Response([], status=status.HTTP_200_OK)

    usuario_comercial_qs = UsuarioAreaComercial.objects.filter(usuario_id=id).select_related('area_comercial')

    # Criar um conjunto para armazenar loja_codigo já vistos
    seen = set()
    unique_results = []

    for obj in usuario_comercial_qs:
        loja_codigo = obj.area_comercial.loja_codigo
        if loja_codigo not in seen:
            seen.add(loja_codigo)
            unique_results.append(obj)

    # Se unique_results estiver vazio, ainda retornamos a lista vazia
    serializer = UsuarioAreaComercialSerializer(unique_results, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)