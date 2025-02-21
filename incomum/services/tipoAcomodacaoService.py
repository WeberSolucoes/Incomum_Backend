from rest_framework.response import Response
from rest_framework import status
from ..models import *
from ..serializers.tipoAcomodacaoSerializer import *

def findById(id) -> Response:
    try:
        loja: Loja = TipoAcomodacao.objects.get(tac_codigo = id)
    except TipoAcomodacao.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TipoAcomodacaoSerializer(loja)
    return Response(serializer.data)

def create(request) -> Response:
    serializer = TipoAcomodacaoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def update(request, id) -> Response:
    try:
        loja: Loja = TipoAcomodacao.objects.get(tac_codigo = id)
    except TipoAcomodacao.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TipoAcomodacaoSerializer(loja, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def delete(id) -> Response:
    try:
        loja: Loja = TipoAcomodacao.objects.get(tac_codigo = id)
    except TipoAcomodacao.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    loja.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

def list_all() -> Response:
    lojas = TipoAcomodacao.objects.all().order_by('tac_descricao')
    serializer = TipoAcomodacaoSerializer(lojas, many=True)
    return Response(serializer.data)
