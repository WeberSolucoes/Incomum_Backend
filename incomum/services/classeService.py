from rest_framework.response import Response
from rest_framework import status
from ..models import *
from ..serializers.classeSerializer import *

def findById(id) -> Response:
    try:
        loja: Loja = Classe.objects.get(cla_codigo = id)
    except Classe.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ClasseSerializer(loja)
    return Response(serializer.data)

def create(request) -> Response:
    serializer = ClasseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def update(request, id) -> Response:
    try:
        loja: Loja = Classe.objects.get(cla_codigo = id)
    except Classe.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ClasseSerializer(loja, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def delete(id) -> Response:
    try:
        loja: Loja = Classe.objects.get(cla_codigo = id)
    except Classe.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    loja.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

def list_all() -> Response:
    lojas = Classe.objects.all().order_by('cla_descricao')
    serializer = ClasseSerializer(lojas, many=True)
    return Response(serializer.data)
