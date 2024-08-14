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

from autenticacaoWeber.models.usuario import *
from incomum.serializers.vendedorSerializer import VendedorSerializer
from incomum.serializers import agenciaSerializer

from ..models import *
from ..serializers.relatorioSerializer import *


def total_byfilter(request) -> Response:
    data_inicio = request.query_params.get("dataInicio")
    data_fim = request.query_params.get("dataFim")

    usuario_id = request.query_params.get("usuario_id")
    user_unidades = list_all_lojas_byfilter(usuario_id).data
    user_unidades = [id["loj_codigo"] for id in user_unidades]

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
        Relatorio.objects.filter(fim_data__range=[data_inicio, data_fim])
        .filter(loj_codigo__in=user_unidades)
        .values("fim_valorliquido", "fim_valorinc", "fim_valorincajustado")
    )
    if len(unidades) > 0:
        relatorios = relatorios.filter(loj_codigo__in=unidades)

    if len(areaComerciais) > 0:
        relatorios = relatorios.filter(aco_codigo__in=areaComerciais)

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


def list_all_byfilter(request) -> Response:
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
        relatorios = relatorios.filter(loj_codigo__in=unidades)

    if areaComerciais:
        relatorios = relatorios.filter(aco_codigo__in=areaComerciais)

    if agencias:
        relatorios = relatorios.filter(age_codigo__in=agencias)

    if vendedores:
        relatorios = relatorios.filter(ven_codigo__in=vendedores)

    paginator = PageNumberPagination()
    paginator.page_size = request.query_params.get("pageSize", 10)
    paginated_relatorios = paginator.paginate_queryset(relatorios, request)
    serializer = RelatorioSerializer(paginated_relatorios, many=True)
    return paginator.get_paginated_response(serializer.data)


def list_all_lojas_byfilter(id) -> Response:
    areasId = AreaComercial.objects.filter(usuarioareacomercial__usuario_id=id)
    lojas_id = set(areasId.values_list("loja_codigo", flat=True))
    lojas = Loja.objects.filter(loj_codigo__in=lojas_id).values(
        "loj_codigo", "loj_descricao"
    )

    return Response(lojas)


def list_all_areas_byfilter(request, id) -> Response:
    areas = AreaComercial.objects.filter(usuarioareacomercial__usuario_id=id).values(
        "aco_codigo", "aco_descricao"
    )
    unidades = request.query_params.getlist("unidade")

    if len(unidades) > 0:
        areas = areas.filter(loja_codigo__in=unidades)

    return Response(areas)


def list_all_vendedores_byfilter(request, id) -> Response:
    user = Usuario.objects.get(id=id)
    if user.groups.filter(name="Vendedor").exists():
        data = {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
        }
        return Response(data=data)
    else:
        unidades = request.query_params.getlist("unidade")
        print(unidades)
        if len(unidades) == 0:
            return Response(
                {"message": "O parâmetro unidade é obrigatório."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        # procuro as areas comercias filtrando pela unidade
        # acho os usuarios pela area comercial
        # verifico quais usuario sao vendedores e voalá
        areas = AreaComercial.objects.filter(loja_codigo__in=unidades)
        usuarios = UsuarioAreaComercial.objects.filter(area_comercial__in=areas)
        usuarios = Usuario.objects.filter(
            id__in=usuarios.values_list("usuario_id", flat=True)
        )
        vendedores = usuarios.filter(groups__name="Vendedor").values(
            "id", "first_name", "last_name"
        )

        return Response(vendedores)


def list_all_agencias_byfilter(request, id) -> Response:
    areas = AreaComercial.objects.filter(
        usuarioareacomercial__usuario_id=id
    ).values_list("aco_codigo", flat=True)
    agencias = Agencia.objects.filter(aco_codigo__in=areas).values(
        "age_codigo", "age_descricao"
    )

    areasComerciais = request.query_params.getlist("areaComercial")

    if len(areasComerciais) > 0:
        agencias = agencias.filter(aco_codigo__in=areasComerciais)

    return Response(agencias)

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
            relatorio.fim_data,
            relatorio.fim_markup,
            locale.currency(relatorio.fim_valorinc, grouping=True),
            locale.currency(relatorio.fim_valorincajustado, grouping=True),
            relatorio.aco_codigo.aco_descricao,
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

    usuario_id = request.query_params.get("usuario_id")
    user_unidades = list_all_lojas_byfilter(usuario_id).data
    user_unidades = [id["loj_codigo"] for id in user_unidades]

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

    relatorios = Relatorio.objects.filter(fim_data__range=[data_inicio, data_fim]).filter(loj_codigo__in=user_unidades)
    if unidades:
        relatorios = relatorios.filter(loj_codigo__in=unidades)

    if areaComerciais:
        relatorios = relatorios.filter(aco_codigo__in=areaComerciais)

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
    planilha_titulo = f"Relatorio_{Usuario.objects.get(id=usuario_id).first_name}_{data_inicio.date()}_{data_fim.date()}"
    ws.title = planilha_titulo

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


