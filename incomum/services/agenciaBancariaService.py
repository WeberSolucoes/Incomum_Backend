from rest_framework import status
from rest_framework.response import Response
from ..models.agenciaBancaria import AgenciaBancaria
from ..serializers.agenciaBancariaSerializer import AgenciaBancariaSerializer

def find_by_id(id):
    try:
        entity = AgenciaBancaria.objects.get(age_codigo=id)
        return Response(AgenciaBancariaSerializer(entity).data, status=status.HTTP_200_OK)
    except AgenciaBancaria.DoesNotExist:
        return Response({"error": "Agência Bancária não encontrada"}, status=status.HTTP_404_NOT_FOUND)

def list_all():
    entities = AgenciaBancaria.objects.all()
    return Response(AgenciaBancariaSerializer(entities, many=True).data, status=status.HTTP_200_OK)

def create(request):
    serializer = AgenciaBancariaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def update(request, id):
    try:
        agencia_bancaria = AgenciaBancaria.objects.get(age_codigo=id)
    except AgenciaBancaria.DoesNotExist:
        return Response({"error": "Agência Bancária não encontrada"}, status=status.HTTP_404_NOT_FOUND)

    serializer = AgenciaBancariaSerializer(agencia_bancaria, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def delete(id):
    try:
        agencia_bancaria = AgenciaBancaria.objects.get(age_codigo=id)
    except AgenciaBancaria.DoesNotExist:
        return Response({"error": "Agência Bancária não encontrada"}, status=status.HTTP_404_NOT_FOUND)

    agencia_bancaria.delete()
    return Response({"message": "Agência Bancária deletada com sucesso"}, status=status.HTTP_204_NO_CONTENT)
