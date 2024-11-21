from rest_framework.response import Response
from rest_framework import status
from ..models import *
from ..serializers.lojaComercialSerializer import *

def findById(id) -> Response:
    try:
        lojaComercial: LojaComercial = LojaComercial.objects.get(loj_codigo = id)
    except LojaComercial.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = LojaComercialSerializer(lojaComercial)
    return Response(serializer.data)

def create(request) -> Response:
    serializer = LojaComercialSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def update(request, id) -> Response:
    try:
        lojaComercial: LojaComercial = LojaComercial.objects.get(loj_codigo = id)
    except LojaComercial.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = LojaComercialSerializer(lojaComercial, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def delete(id) -> Response:
    try:
        lojaComercial: LojaComercial = LojaComercial.objects.get(loj_codigo = id)
    except LojaComercial.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    lojaComercial.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

def list_all() -> Response:
    lojasComercial = LojaComercial.objects.all()
    serializer = LojaComercialSerializer(lojasComercial, many=True)
    return Response(serializer.data)