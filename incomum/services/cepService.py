from rest_framework.response import Response
from rest_framework import status
from ..models import *
from ..serializers.cepSerializer import *

def findById(id) -> Response:
    try:
        loja: Loja = Cep.objects.get(cep_codigo = id)
    except Cep.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CepSerializer(loja)
    return Response(serializer.data)

def create(request) -> Response:
    serializer = CepSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def update(request, id) -> Response:
    try:
        loja: Loja = Cep.objects.get(cep_codigo = id)
    except Cep.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CepSerializer(loja, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def delete(id) -> Response:
    try:
        loja: Loja = Cep.objects.get(cep_codigo = id)
    except Cep.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    loja.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

def list_all() -> Response:
    lojas = Cep.objects.all()
    serializer = CepSerializer(lojas, many=True)
    return Response(serializer.data)
