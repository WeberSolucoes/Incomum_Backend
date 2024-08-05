from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from incomum.mappers import relatorioMapper
from ..models import *
from ..serializers.relatorioSerializer import *

class FaturamentoSimplificadoPagination(PageNumberPagination):
    page_size = 10 

def listByFilters(request):
    serializer = RelatorioFiltersSerializer(data=request.data)
    if serializer.is_valid():
        data_inicio = serializer.validated_data['dataInicio']
        data_fim = serializer.validated_data['dataFim']
        loja = serializer.validated_data.get('loja')
        area_comercial = serializer.validated_data.get('areaComercial')
        agencia = serializer.validated_data.get('agencia')
        vendedor = serializer.validated_data.get('vendedor')

        query = FaturamentoSimplificado.objects.filter(fim_data__range=[data_inicio, data_fim])
        if loja is not None:
            query = query.filter(loj_codigo=loja)
        if area_comercial is not None:
            query = query.filter(aco_codigo=area_comercial)
        if agencia is not None:
            query = query.filter(age_codigo=agencia)
        if vendedor is not None:
            query = query.filter(ven_codigo=vendedor)
        totalLiqVenda = 0
        totalInc = 0
        totalIncAjustado = 0
        for q in query:
            totalLiqVenda += q.fim_valorliquido
            totalInc += q.fim_valorinc
            totalIncAjustado += q.fim_valorincajustado
        print(f"{totalLiqVenda:.2f}, {totalInc:.2f}, {totalIncAjustado:.2f}")

        paginator = FaturamentoSimplificadoPagination()
        page = paginator.paginate_queryset(query, request)
        if page is not None:
            resultados = relatorioMapper.entitiesToDtos(page)
            return paginator.get_paginated_response({"totalLiqVenda": totalLiqVenda, "totalInc": totalInc, "totalIncAjustado": totalIncAjustado,"data": resultados.data})
        resultados = relatorioMapper.entitiesToDtos(query)
        return Response(resultados.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

