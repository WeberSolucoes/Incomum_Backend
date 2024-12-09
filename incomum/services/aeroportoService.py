from rest_framework import status
from rest_framework.response import Response
from ..models import *
from ..serializers.aeroportoSerializer import *

from django.db import connection
import traceback

import base64
from django.http import JsonResponse, Http404
from django.shortcuts import get_object_or_404

def find_by_id(id):
    entity = Aeroporto.objects.get(age_codigo=id)
    return Response(AeroportoSerializer(entity).data, status=status.HTTP_200_OK)

def list_all():
    entities = Aeroporto.objects.all()
    return Response(AeroportoSerializer(entities, many=True).data, status=status.HTTP_200_OK)

def create(request):
    serializer = AeroportoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def update(request, id):
    try:
        agencia: Agencia = Aeroporto.objects.get(age_codigo=id)
    except Agencia.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    print("Dados recebidos para atualização:", request.data)
    serializer = AeroportoSerializer(agencia, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def delete(id):
    try:
        agencia: Agencia = Aeroporto.objects.get(age_codigo=id)
    except Agencia.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    agencia.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

