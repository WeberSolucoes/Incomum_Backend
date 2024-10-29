from rest_framework import status
from rest_framework.response import Response
from ..models.agente import Agente
from ..serializers.agenteSerializer import AgenteSerializer

def find_by_id(id):
    entity = Agente.objects.get(agt_codigo=id)
    return Response(AgenteSerializer(entity).data, status=status.HTTP_200_OK)

def list_all():
    entities = Agente.objects.all()
    return Response(AgenteSerializer(entities, many=True).data, status=status.HTTP_200_OK)

def create(request):
    serializer = AgenteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def update(request, id):
    try:
        agente: Agente = Agente.objects.get(agt_codigo=id)
    except Agente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = AgenteSerializer(agente, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def delete(id):
    try:
        agente: Agente = Agente.objects.get(agt_codigo=id)
    except Agente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    agente.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
