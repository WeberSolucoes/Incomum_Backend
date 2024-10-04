from concurrent.futures import ThreadPoolExecutor
import datetime
from django.http import HttpResponse
import openpyxl
from openpyxl import Workbook, load_workbook
import io
import os
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from incomum.serializers.vendedorSerializer import VendedorSerializer
from incomum.serializers import agenciaSerializer
from incomum.serializers.lojaSerializer import LojaSerializer

from ..models import *
from ..serializers.relatorioSerializer import *


def total_byfilter(request) -> Response:
    data_inicio = request.query_params.get("dataInicio")
    data_fim = request.query_params.get("dataFim")


    if data_inicio is None or data_fim is None:
        return Response(
            {"message": "Os parâmetros data inicial e data final são obrigatórios."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        data_inicio = datetime.datetime.strptime(data_inicio, "%d-%m-%Y")
        data_fim = datetime.datetime.strptime(data_fim, "%d-%m-%Y")
        if data_fim < data_inicio:
            return Response(
                {"message": "A data final deve ser maior que a data inicial."},
                status=status.HTTP_400_BAD_REQUEST,
            )
    except ValueError:
        return Response(
            {"message": "Data inválida. Use o formato DD-MM-YYYY."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    unidades = request.query_params.getlist("unidade")
    areaComerciais = request.query_params.getlist("areaComercial")
    agencias = request.query_params.getlist("agencia")
    vendedores = request.query_params.getlist("vendedor")

    relatorios = (
        Relatorio.objects.all()
    )
    if len(unidades) > 0:
        relatorios = relatorios.all()

    if len(areaComerciais) > 0:
        relatorios = relatorios.all()

    if len(agencias) > 0:
        relatorios = relatorios.filter(age_codigo__in=agencias)

    if len(vendedores) > 0:
        relatorios = relatorios.filter(ven_codigo__in=vendedores)
    totais = relatorios.aggregate(
        total_valorliquido=Sum("fim_valorliquido"),
        total_valorinc=Sum("fim_valorinc"),
        total_valorincajustado=Sum("fim_valorincajustado"),
    )
    if totais["total_valorliquido"] is None:
        totais["total_valorliquido"] = 0
    if totais["total_valorinc"] is None:
        totais["total_valorinc"] = 0
    if totais["total_valorincajustado"] is None:
        totais["total_valorincajustado"] = 0
    totais["total_valorliquido"] = locale.currency(
        totais["total_valorliquido"], grouping=True
    )
    totais["total_valorinc"] = locale.currency(totais["total_valorinc"], grouping=True)
    totais["total_valorincajustado"] = locale.currency(
        totais["total_valorincajustado"], grouping=True
    )
    return Response(totais, status=status.HTTP_200_OK)

def list_all_byfilter(request):
    # Obtenha os parâmetros da requisição
    data_inicio = request.GET.get('dataInicio')
    data_fim = request.GET.get('dataFim')
    unidades = request.GET.get('unidades')
    areas_comerciais = request.GET.get('areasComerciais')
    agencias = request.GET.get('agencias')
    vendedores = request.GET.get('vendedores')

    queryset = Relatorio.objects.all()  # Inicie com todos os registros

    # Filtre pela data
    if data_inicio and data_fim:
        queryset = queryset.filter(fim_data__gte=data_inicio, fim_data__lte=data_fim)

    # Filtre por unidades
    if unidades:
        unidade_ids = unidades.split(',')
        queryset = queryset.filter(loj_codigo__in=unidade_ids)

    # Filtre por áreas comerciais
    if areas_comerciais:
        area_ids = areas_comerciais.split(',')
        queryset = queryset.filter(aco_codigo__in=area_ids)

    # Filtre por agências
    if agencias:
        agencia_ids = agencias.split(',')
        queryset = queryset.filter(age_codigo__in=agencia_ids)

    # Filtre por vendedores
    if vendedores:
        vendedor_ids = vendedores.split(',')
        queryset = queryset.filter(ven_codigo__in=vendedor_ids)

    # Serialização e retorno dos dados
    serializer = RelatorioSerializer(queryset, many=True)
    return Response(serializer.data)



def list_all_lojas_byfilter(request):
    # Filtrar as lojas conforme necessário, por exemplo:
    # lojas = Loja.objects.filter(user=request.user)
    lojas = Loja.objects.all()  # Obtém todas as lojas

    # Serializa as lojas
    serializer = LojaSerializer(lojas, many=True)

    # Retorna a resposta com os dados serializados
    return Response(serializer.data)

def list_all_areas_byfilter(request) -> Response:
    areas = AreaComercial.objects.all().values('aco_descricao','aco_codigo')  # Carrega as lojas relacionadas
    return Response(areas)



def list_all_vendedores_byfilter(request):
    # Filtre os vendedores conforme necessário, por exemplo:
    # vendedores = Vendedor.objects.filter(some_condition)
    vendedores = Vendedor.objects.all()  # Obtém todos os vendedores

    # Serializa os vendedores
    serializer = VendedorSerializer(vendedores, many=True)

    # Retorna a resposta com os dados serializados
    return Response(serializer.data)

def list_all_agencias_byfilter(request) -> Response:
    agencias = Agencia.objects.all().values("age_codigo", "age_descricao")
    areasComerciais = request.query_params.getlist("areaComercial")

    if areasComerciais:
        agencias = agencias.all()

    return Response(agencias)



def create_excel_byfilter(request) -> Response:
    data_inicio = request.query_params.get("dataInicio")
    data_fim = request.query_params.get("dataFim")

    if data_inicio is None or data_fim is None:
        return Response(
            {"message": "Os parâmetros data inicial e data final são obrigatórios."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        data_inicio = datetime.datetime.strptime(data_inicio, "%d-%m-%Y")
        data_fim = datetime.datetime.strptime(data_fim, "%d-%m-%Y")
        if data_fim < data_inicio:
            return Response(
                {"message": "A data final deve ser maior que a data inicial."},
                status=status.HTTP_400_BAD_REQUEST,
            )
    except ValueError:
        return Response(
            {"message": "Data inválida. Use o formato DD-MM-YYYY."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    unidades = request.query_params.getlist("unidade")
    areaComerciais = request.query_params.getlist("areaComercial")
    agencias = request.query_params.getlist("agencia")
    vendedores = request.query_params.getlist("vendedor")

    relatorios = Relatorio.objects.filter(fim_data__range=[data_inicio, data_fim])
    if unidades:
        relatorios = relatorios.all()

    if areaComerciais:
        relatorios = relatorios.all()

    if agencias:
        relatorios = relatorios.filter(age_codigo__in=agencias)

    if vendedores:
        relatorios = relatorios.filter(ven_codigo__in=vendedores)

    return response

    # Processa os chunks e cria o Excel conforme a implementação anterior.
    # Código restante da geração do arquivo Excel




def process_data_chunk(data_chunk):
    wb = Workbook()
    ws = wb.active
    headers = [
        'Tipo',
        'Núm. Venda',
        'Num. Pct',
        'Valor Liquido Venda',
        'Data',
        'MarkUp',
        'Income',
        'Income Ajustado',
        'Área Comercial',
        'Agência',
        'Vendedor'
    ]
    ws.append(headers)

    for relatorio in data_chunk:
        ws.append([
            relatorio.fim_tipo,
            relatorio.tur_numerovenda,
            relatorio.tur_codigo,
            locale.currency(relatorio.fim_valorliquido, grouping=True),
            relatorio.fim_data.strftime('%d/%m/%Y'),
            round(relatorio.fim_markup, 4),
            locale.currency(relatorio.fim_valorinc, grouping=True),
            locale.currency(relatorio.fim_valorincajustado, grouping=True),
            relatorio.age_codigo.age_descricao,
            relatorio.ven_codigo.ven_descricao
        ])

    buffer = io.BytesIO()
    wb.save(buffer)
    buffer.seek(0)
    return buffer.getvalue()

def create_excel_byfilter(request) -> Response:
    data_inicio = request.query_params.get("dataInicio")
    data_fim = request.query_params.get("dataFim")

    if data_inicio is None or data_fim is None:
        return Response(
            {"message": "Os parâmetros data inicial e data final são obrigatórios."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        data_inicio = datetime.datetime.strptime(data_inicio, "%d-%m-%Y")
        data_fim = datetime.datetime.strptime(data_fim, "%d-%m-%Y")
        if data_fim < data_inicio:
            return Response(
                {"message": "A data final deve ser maior que a data inicial."},
                status=status.HTTP_400_BAD_REQUEST,
            )
    except ValueError:
        return Response(
            {"message": "Data inválida. Use o formato DD-MM-YYYY."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    unidades = request.query_params.getlist("unidade")
    areaComerciais = request.query_params.getlist("areaComercial")
    agencias = request.query_params.getlist("agencia")
    vendedores = request.query_params.getlist("vendedor")

    relatorios = Relatorio.objects.all()
    if unidades:
        relatorios = relatorios.all()

    if areaComerciais:
        relatorios = relatorios.all()

    if agencias:
        relatorios = relatorios.filter(age_codigo__in=agencias)

    if vendedores:
        relatorios = relatorios.filter(ven_codigo__in=vendedores)

    # Divide os dados em chunks
    num_chunks = os.cpu_count() or 4
    chunk_size = len(relatorios) // num_chunks or 1
    data_chunks = [relatorios[i:i + chunk_size] for i in range(0, len(relatorios), chunk_size)]

    # Processa os chunks em paralelo
    with ThreadPoolExecutor(max_workers=num_chunks) as executor:
        results = list(executor.map(process_data_chunk, data_chunks))

    wb = Workbook()
    ws = wb.active
    headers = [
        'Tipo',
        'Núm. Venda',
        'Num. Pct',
        'Valor Liquido Venda',
        'Data',
        'MarkUp',
        'Income',
        'Income Ajustado',
        'Área Comercial',
        'Agência',
        'Vendedor'
    ]
    ws.append(headers)
    # Cria o Excel final
    ws.title = 'teste'

    for result in results:
        buffer = io.BytesIO(result)
        wb_part = load_workbook(buffer)
        ws_part = wb_part.active  # Assume que cada chunk tem apenas uma planilha
        for row in ws_part.iter_rows(min_row=2, values_only=True):  # Pula o cabeçalho
            ws.append(row)

    # Adiciona totais
    totais = total_byfilter(request).data
    colunas = [4, 7, 8]
    nomes = ['Total Valor Liquido', 'Total Income', 'Total Income Ajustado']
    for i, chave in enumerate(totais.keys()):
        ws.cell(row=len(relatorios) + 3, column=colunas[i]).value = nomes[i]
        ws.cell(row=len(relatorios) + 4, column=colunas[i]).value = totais[chave]

    buffer = io.BytesIO()
    wb.save(buffer)
    buffer.seek(0)

    response = HttpResponse(buffer.getvalue(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response['Content-Disposition'] = f'attachment; filename="{planilha_titulo}.xlsx"'
    return response



def list_all_areas(request) -> Response:
    areas = AreaComercial.objects.all()
    return Response(list(areas))
