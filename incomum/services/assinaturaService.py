from rest_framework.response import Response
from rest_framework import status
from ..models import *
from ..serializers.assinaturaSerializer import *
from ..serializers.companhiaSerializer import *

def findById(id) -> Response:
    try:
        loja: Loja = Assinatura.objects.get(ass_codigo = id)
    except Assinatura.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = AssinaturaSerializer(loja)
    return Response(serializer.data)

def create(request) -> Response:
    serializer = AssinaturaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def update(request, id) -> Response:
    try:
        loja: Loja = Assinatura.objects.get(ass_codigo = id)
    except Assinatura.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = AssinaturaSerializer(loja, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def delete(id) -> Response:
    try:
        loja: Loja = Assinatura.objects.get(com_codigo = id)
    except Assinatura.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    loja.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

def list_all() -> Response:
    lojas = Assinatura.objects.all()
    serializer = AssinaturaSerializer(lojas, many=True)
    return Response(serializer.data)


def list_all_companhia() -> Response:
    companhia = Companhia.objects.all()
    serializer = CompanhiaSerializer(companhia, many=True)
    return Response(serializer.data)
