from rest_framework.response import Response
from rest_framework import status
from ..models import *
from ..serializers.parceiroSerializer import *

def findById(id) -> Response:
    try:
        loja: Loja = Parceiro.objects.get(par_codigo = id)
    except Parceiro.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ParceiroSerializer(loja)
    return Response(serializer.data)

def create(request) -> Response:
    serializer = ParceiroSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def update(request, id) -> Response:
    try:
        loja: Loja = Parceiro.objects.get(par_codigo = id)
    except Parceiro.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ParceiroSerializer(loja, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def delete(id) -> Response:
    try:
        loja: Loja = Parceiro.objects.get(par_codigo = id)
    except Parceiro.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    loja.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

def list_all() -> Response:
    lojas = Parceiro.objects.all()
    serializer = ParceiroSerializer(lojas, many=True)
    return Response(serializer.data)
