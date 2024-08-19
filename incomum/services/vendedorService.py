from rest_framework import status
from rest_framework.response import Response
from ..models import Vendedor
from ..serializers.vendedorSerializer import VendedorSerializer

def find_by_id(id):
    entity = Vendedor.objects.get(ven_codigo=id)
    return Response(VendedorSerializer(entity).data, status=status.HTTP_200_OK)

def list_all():
    entities = Vendedor.objects.all()
    return Response(VendedorSerializer(entities, many=True).data, status=status.HTTP_200_OK)

def create(request):
    serializer = VendedorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def update(request, id):
    try:
        agencia: Vendedor = Vendedor.objects.get(ven_codigo=id)
    except Vendedor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = VendedorSerializer(agencia, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def delete(id):
    try:
        agencia: Vendedor = Vendedor.objects.get(ven_codigo=id)
    except Vendedor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    agencia.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
