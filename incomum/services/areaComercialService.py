from rest_framework.response import Response
from rest_framework import status
from ..models import *
from ..serializers.areaComercialSerializer import *

def findById(id) -> Response:
    try:
        area: AreaComercial = AreaComercial.objects.get(aco_codigo = id)
    except AreaComercial.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = AreaComercialSerializer(area)
    return Response(serializer.data)

def create(request) -> Response:
    serializer = AreaComercialCreateSerializer(data=request.data)
    if serializer.is_valid():
        try:
            loja: Loja = Loja.objects.get(loj_codigo = serializer.validated_data['id_loja'])

            area: AreaComercial = AreaComercial()
            area.aco_descricao = serializer.validated_data['aco_descricao']
            area.aco_rateio = serializer.validated_data['aco_rateio']
            area.aco_situacao = serializer.validated_data['aco_situacao']
            area.loja_codigo = loja
            area.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Loja.DoesNotExist:
            return Response({'message': 'Loja não encontrada.'},status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
def findByLoja(id) -> Response:
    try:
        loja = Loja.objects.get(loj_codigo = id)
        areas = AreaComercial.objects.filter(loja_codigo = loja)
        serializer = AreaComercialSerializer(areas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Loja.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
def update(request, id) -> Response:
    serializer = AreaComercialCreateSerializer(data=request.data)
    if serializer.is_valid():
        try:
            area: AreaComercial = AreaComercial.objects.get(aco_codigo = id)
            loja: Loja = Loja.objects.get(loj_codigo = serializer.validated_data['id_loja'])

            area.aco_descricao = serializer.validated_data['aco_descricao'] if serializer.validated_data['aco_descricao'] else area.aco_descricao
            area.aco_rateio = serializer.validated_data['aco_rateio'] if serializer.validated_data['aco_rateio'] else area.aco_rateio
            area.aco_situacao = serializer.validated_data['aco_situacao'] if serializer.validated_data['aco_situacao'] else area.aco_situacao
            area.loja_codigo = loja
            area.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        except AreaComercial.DoesNotExist or Loja.DoesNotExist:
            return Response({'message': 'AreaComercial ou Loja não encontrada.'},status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
def delete(id) -> Response:
    try:
        area: AreaComercial = AreaComercial.objects.get(aco_codigo = id)
    except AreaComercial.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    area.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
def list_all() -> Response:
    areas = AreaComercial.objects.all()
    serializer = AreaComercialSerializer(areas, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)