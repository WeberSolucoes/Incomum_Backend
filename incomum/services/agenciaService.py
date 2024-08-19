from rest_framework import status
from rest_framework.response import Response
from ..models import Agencia
from ..serializers.agenciaSerializer import AgenciaSerializer

def find_by_id(id):
    entity = Agencia.objects.get(age_codigo=id)
    return Response(AgenciaSerializer(entity).data, status=status.HTTP_200_OK)

def list_all():
    entities = Agencia.objects.all()
    return Response(AgenciaSerializer(entities, many=True).data, status=status.HTTP_200_OK)

def create(request):
    serializer = AgenciaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def update(request, id):
    try:
        agencia: Agencia = Agencia.objects.get(age_codigo=id)
    except Agencia.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = AgenciaSerializer(agencia, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def delete(id):
    try:
        agencia: Agencia = Agencia.objects.get(age_codigo=id)
    except Agencia.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    agencia.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
