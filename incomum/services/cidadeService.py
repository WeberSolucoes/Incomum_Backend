from rest_framework.response import Response
from rest_framework import status
from ..models import *
from ..serializers.cidadeSerializer import *

def findById(id) -> Response:
    try:
        loja: Loja = Cidade.objects.get(cid_codigo = id)
    except Cidade.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CidadeSerializer(loja)
    return Response(serializer.data)

def create(request) -> Response:
    serializer = CidadeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def update(request, id) -> Response:
    try:
        loja: Loja = Cidade.objects.get(cid_codigo = id)
    except Cidade.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CidadeSerializer(loja, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def delete(id) -> Response:
    try:
        loja: Loja = Cidade.objects.get(cid_codigo = id)
    except Cidade.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    loja.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

def list_all() -> Response:
    lojas = Cidade.objects.all()[:20]
    serializer = CidadeSerializer(lojas, many=True)
    return Response(serializer.data)
