from rest_framework.response import Response
from rest_framework import status
from ..models import *
from ..serializers.companhiaSerializer import *

def findById(id) -> Response:
    try:
        loja: Loja = Companhia.objects.get(com_codigo = id)
    except Companhia.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CompanhiaSerializer(loja)
    return Response(serializer.data)

def create(request) -> Response:
    serializer = CompanhiaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def update(request, id) -> Response:
    try:
        loja: Loja = Companhia.objects.get(com_codigo = id)
    except Companhia.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CompanhiaSerializer(loja, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def delete(id) -> Response:
    try:
        loja: Loja = Companhia.objects.get(com_codigo = id)
    except Companhia.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    loja.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

def list_all() -> Response:
    lojas = Companhia.objects.all().order_by('com_descricao')
    serializer = CompanhiaSerializer(lojas, many=True)
    return Response(serializer.data)
