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
from django.contrib.auth.models import User
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from incomum.serializers.vendedorSerializer import VendedorSerializer
from incomum.serializers import agenciaSerializer
from incomum.serializers.relatorioSerializer import RelatorioSerializer
from incomum.serializers.lojaSerializer import LojaSerializer
from incomum.serializers.areaComercialSerializer import AreaComercialSerializer
from datetime import datetime
from django.db import connection
from django.core.paginator import Paginator

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
    user_id = request.user.id
    data_consulta = request.GET.get('dataInicio')
    data_consulta_final = request.GET.get('dataFim')
    unidade_selecionada = request.GET.get('unidades')
    areas_selecionadas = request.GET.getlist('areasComerciais')
    agencia_selecionada = request.GET.get('agencias')
    vendedor_selecionada = request.GET.get('vendedores')

    # Consultando as áreas do usuário
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT ac.aco_codigo
            FROM usuariocomercial ac
            INNER JOIN auth_user uac ON uac.id = ac.usr_codigo
            WHERE uac.id = %s
        """, [user_id])
        user_areas = [row[0] for row in cursor.fetchall()]

    # Validando as datas
    try:
        data_consulta_dt = datetime.strptime(data_consulta, "%Y-%m-%d")
        data_consulta_final_dt = datetime.strptime(data_consulta_final, "%Y-%m-%d")
    except ValueError:
        return Response(
            {"message": "Datas inválidas. Use o formato YYYY-MM-DD."},
            status=status.HTTP_400_BAD_REQUEST
        )

    query = """
        SELECT fim_tipo, tur_numerovenda, tur_codigo, fim_valorliquido, fim_data, fim_markup, fim_valorinc, fim_valorincajustado, aco_descricao, age_descricao, ven_descricao, fat_valorvendabruta
        FROM faturamentosimplificado 
        WHERE fim_data BETWEEN %s AND %s 
    """
    params = [data_consulta_dt, data_consulta_final_dt]

    # Inclua a condição aco_codigo somente se user_areas não estiver vazio
    if user_areas:
        query += " AND aco_codigo IN %s"
        params.append(tuple(user_areas))

    if unidade_selecionada:
        query += " AND loj_codigo = %s"
        params.append(unidade_selecionada)

    if areas_selecionadas:
        query += " AND aco_codigo IN %s"
        params.append(tuple(areas_selecionadas))

    if agencia_selecionada:
        query += " AND age_codigo = %s"
        params.append(agencia_selecionada)

    if vendedor_selecionada:
        query += " AND ven_codigo = %s"
        params.append(vendedor_selecionada)

    query += " ORDER BY fim_data"

    # Executa a consulta e formata os resultados
    with connection.cursor() as cursor:
        cursor.execute(query, params)
        resultados = cursor.fetchall()

    # Formatando os resultados em dicionários
    resultados_formatados = [{
        'fim_tipo': resultado[0],
        'tur_numerovenda': resultado[1],
        'tur_codigo': resultado[2],
        'fim_valorliquido': resultado[3],
        'fim_data': resultado[4],
        'fim_markup': resultado[5],
        'fim_valorinc': resultado[6],
        'fim_valorincajustado': resultado[7],
        'aco_descricao': resultado[8],
        'age_descricao': resultado[9],
        'ven_descricao': resultado[10],
        'fat_valorvendabruta': resultado[11],
    } for resultado in resultados]

    # Paginação
    paginator = Paginator(resultados_formatados, 100000)  # 100 resultados por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Calculando as somas após aplicar os filtros
    soma_totais = {
        'total_valorinc': sum(item['fim_valorinc'] for item in resultados_formatados if item['fim_valorinc'] is not None),
        'total_valorincajustado': sum(item['fim_valorincajustado'] for item in resultados_formatados if item['fim_valorincajustado'] is not None),
        'total_valorliquido': sum(item['fim_valorliquido'] for item in resultados_formatados if item['fim_valorliquido'] is not None),
    }

    return Response({
        'resultados': [RelatorioSerializer(resultado).data for resultado in page_obj],
        'num_paginas': paginator.num_pages,
        'pagina_atual': page_obj.number,
        'has_next': page_obj.has_next(),
        'has_previous': page_obj.has_previous(),
        'soma_totais': soma_totais,
    }, status=status.HTTP_200_OK)



def list_all_lojas_byfilter(request):
    # Filtrar as lojas conforme necessário, por exemplo:
    # lojas = Loja.objects.filter(user=request.user)
    lojas = Loja.objects.all().order_by('loj_descricao')  # Obtém todas as lojas

    # Serializa as lojas
    serializer = LojaSerializer(lojas, many=True)

    # Retorna a resposta com os dados serializados
    return Response(serializer.data)

def list_all_areas_byfilter(request) -> Response:
    user_id = request.user.id

    # Verificar áreas comerciais associadas ao usuário
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT ac.aco_codigo, a.aco_descricao
            FROM usuariocomercial ac
            INNER JOIN areacomercial a ON a.aco_codigo = ac.aco_codigo
            WHERE ac.usr_codigo = %s
        """, [user_id])
        user_areas = cursor.fetchall()

    if request.method == 'GET':
        unidade_selecionada = request.GET.get('unidade')

        if user_areas:
            # Se o usuário tem áreas associadas, mostrar apenas essas áreas
            associacoes = [
                {'aco_codigo': row[0], 'aco_descricao': row[1]}
                for row in user_areas
            ]
        else:
            # Se o usuário não tem áreas associadas, realizar a consulta com base na unidade
            with connection.cursor() as cursor:
                if unidade_selecionada:
                    cursor.execute("""
                        SELECT lc.aco_codigo, a.aco_descricao
                        FROM lojacomercial lc
                        INNER JOIN areacomercial a ON lc.aco_codigo = a.aco_codigo
                        WHERE lc.loj_codigo = %s ORDER BY aco_descricao
                    """, [unidade_selecionada])
                else:
                    cursor.execute("""
                        SELECT a.aco_codigo, a.aco_descricao
                        FROM areacomercial a ORDER BY aco_descricao
                    """)

                resultados = cursor.fetchall()

            # Formatar os resultados como uma lista de dicionários
            associacoes = [
                {'aco_codigo': row[0], 'aco_descricao': row[1]}
                for row in resultados
            ]

        return Response({'associacoes': associacoes})



def list_all_vendedores_byfilter(request):
    user_id = request.user.id  # ID do usuário logado
    unidade_id = request.GET.get('unidade')  # Unidade selecionada, se houver

    vendedores = []

    # Obtém os códigos de áreas comerciais associadas ao usuário logado
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT ac.aco_codigo
            FROM usuariocomercial ac
            INNER JOIN auth_user uac ON uac.id = ac.usr_codigo
            WHERE uac.id = %s
        """, [user_id])
        user_areas = [row[0] for row in cursor.fetchall()]

    # Se uma unidade for selecionada, buscar vendedores por unidade
    if unidade_id:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT DISTINCT v.ven_codigo, v.ven_descricao
                FROM faturamentosimplificado f
                JOIN vendedor v ON v.ven_codigo = f.ven_codigo
                WHERE f.loj_codigo = %s
                ORDER BY v.ven_descricao
            """, [unidade_id])
            vendedores = cursor.fetchall()

    # Caso contrário, retorna todos os vendedores
    else:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT v.ven_codigo, v.ven_descricao
                FROM vendedor v
                ORDER BY v.ven_descricao
            """)
            vendedores = cursor.fetchall()

    vendedores_formatados = [{'ven_codigo': ven[0], 'ven_descricao': ven[1]} for ven in vendedores]

    return Response({'vendedores': vendedores_formatados})


def list_all_agencias_byfilter(request) -> Response:
    user_id = request.user.id  # Obtém o ID do usuário logado

    # Obter o parâmetro area_comercial da consulta
    area_comercial = request.GET.getlist('area_comercial[]')  # Isso captura todos os valores em uma lista

    # Obter o aco_codigo associado ao usuário
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT ac.aco_codigo
            FROM usuariocomercial ac
            INNER JOIN auth_user uac ON uac.id = ac.usr_codigo
            WHERE uac.id = %s
        """, [user_id])
        user_aco_codigos = [row[0] for row in cursor.fetchall()]

    print(f'Usuário aco_codigos: {user_aco_codigos}')
    print(f'Área comercial para filtro: {area_comercial}')

    with connection.cursor() as cursor:
        if area_comercial:
            # Se uma área comercial foi selecionada, filtrar por ela
            cursor.execute("""
                SELECT age_codigo, age_descricao
                FROM agencia
                WHERE aco_codigo IN %s
            """, [tuple(area_comercial)])
        else:
            # Se nenhuma área comercial foi selecionada, verificar user_aco_codigos
            if user_aco_codigos:
                # Filtrar as agências associadas ao(s) aco_codigo do usuário
                cursor.execute("""
                    SELECT age_codigo, age_descricao
                    FROM agencia
                    WHERE aco_codigo IN %s
                """, [tuple(user_aco_codigos)])
            else:
                # Se não há aco_codigos para o usuário, puxar todos os registros
                cursor.execute("""
                    SELECT age_codigo, age_descricao
                    FROM agencia
                """)

        resultados = cursor.fetchall()

    # Formatar os resultados como uma lista de dicionários
    valores = [
        {'age_codigo': row[0], 'age_descricao': row[1]}
        for row in resultados
    ]

    return Response({'valores': valores})


def create_excel_byfilter(request) -> Response:
    user_id = request.user.id
    data_consulta = request.GET.get('dataInicio')
    data_consulta_final = request.GET.get('dataFim')
    unidade_selecionada = request.GET.get('unidades')
    areas_selecionadas = request.GET.getlist('areasComerciais')
    agencia_selecionada = request.GET.get('agencias')
    vendedor_selecionada = request.GET.get('vendedores')

    # Consultando as áreas do usuário
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT ac.aco_codigo
            FROM usuariocomercial ac
            INNER JOIN auth_user uac ON uac.id = ac.usr_codigo
            WHERE uac.id = %s
        """, [user_id])
        user_areas = [row[0] for row in cursor.fetchall()]

    # Validando as datas
    try:
        data_consulta_dt = datetime.strptime(data_consulta, "%Y-%m-%d")
        data_consulta_final_dt = datetime.strptime(data_consulta_final, "%Y-%m-%d")
    except ValueError:
        return Response(
            {"message": "Datas inválidas. Use o formato YYYY-MM-DD."},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Construindo a query base
    query = """
        SELECT fim_tipo, tur_numerovenda, tur_codigo, fim_valorliquido, fim_data, fim_markup, fim_valorinc, fim_valorincajustado, aco_descricao, age_descricao, ven_descricao, fat_valorvendabruta
        FROM faturamentosimplificado 
        WHERE fim_data BETWEEN %s AND %s 
    """
    params = [data_consulta_dt, data_consulta_final_dt]

    # Adicionando filtros à consulta com base nas seleções
    if user_areas:
        query += " AND aco_codigo IN %s"
        params.append(tuple(user_areas))

    if unidade_selecionada:
        query += " AND loj_codigo = %s"
        params.append(unidade_selecionada)

    if areas_selecionadas and len(areas_selecionadas) > 0:
        query += " AND aco_codigo IN %s"
        params.append(tuple(areas_selecionadas))

    if agencia_selecionada:
        query += " AND age_codigo = %s"
        params.append(agencia_selecionada)

    if vendedor_selecionada:
        query += " AND ven_codigo = %s"
        params.append(vendedor_selecionada)

    query += " ORDER BY fim_data"

    # Executando a consulta e obtendo os resultados
    with connection.cursor() as cursor:
        cursor.execute(query, params)
        resultados = cursor.fetchall()

    print(resultados)

    # Formatando os resultados com o serializer
    resultados_formatados = [RelatorioSerializer({
        'fim_tipo': resultado[0],
        'tur_numerovenda': resultado[1],
        'tur_codigo': resultado[2],
        'fim_valorliquido': resultado[3],
        'fim_data': resultado[4],
        'fim_markup': resultado[5],
        'fim_valorinc': resultado[6],
        'fim_valorincajustado': resultado[7],
        'aco_descricao': resultado[8],
        'age_descricao': resultado[9],
        'ven_descricao': resultado[10],
        'fat_valorvendabruta': resultado[11],
    }).data for resultado in resultados]

    # Chamar a função para processar os dados e gerar o Excel
    excel_data = process_data_chunk(resultados_formatados)

    # Retornar o Excel como resposta (pode ser modificado conforme necessário)
    response = HttpResponse(excel_data, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="relatorio.xlsx"'
    return response


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
        'Valor Inc',
        'Inc Ajustado',
        'Area Comercial',
        'Agencia',
        'Vendedor',
        'Valor Venda Bruta'
    ]
    ws.append(headers)

    for relatorio in data_chunk:
        ws.append([
            relatorio['fim_tipo'],
            relatorio['tur_numerovenda'],
            relatorio['tur_codigo'],
            locale.currency(relatorio['fim_valorliquido'], grouping=True),
            relatorio['fim_data'],
            round(relatorio['fim_markup'], 4),
            locale.currency(relatorio['fim_valorinc'], grouping=True),
            locale.currency(relatorio['fim_valorincajustado'], grouping=True),
            relatorio['aco_descricao'],
            relatorio['age_descricao'],
            relatorio['ven_descricao'],
            locale.currency(relatorio['fat_valorvendabruta'], grouping=True),
        ])

    buffer = io.BytesIO()
    wb.save(buffer)
    buffer.seek(0)
    return buffer.getvalue()

def list_all_area(request) -> Response:
    areas = AreaComercial.objects.all()
    serializer = AreaComercialSerializer(areas, many=True)  # Serialize os dados
    return Response(serializer.data)

def list_all_areas(request, unidade_id=None):
    user_id = request.user.id
    unidade_id = request.GET.get('unidade')
    # Verificar áreas comerciais associadas ao usuário
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT ac.aco_codigo, a.aco_descricao
            FROM usuariocomercial ac
            INNER JOIN areacomercial a ON a.aco_codigo = ac.aco_codigo
            WHERE ac.usr_codigo = %s
        """, [user_id])
        user_areas = cursor.fetchall()

    if user_areas:
        associacoes = [
            {'aco_codigo': row[0], 'aco_descricao': row[1]}
            for row in user_areas
        ]
    else:
        # Se o usuário não tem áreas associadas, realizar a consulta com base na unidade
        with connection.cursor() as cursor:
            if unidade_id:
                cursor.execute("""
                    SELECT lc.aco_codigo, a.aco_descricao
                    FROM lojacomercial lc
                    INNER JOIN areacomercial a ON lc.aco_codigo = a.aco_codigo
                    WHERE lc.loj_codigo = %s ORDER BY aco_descricao
                """, [unidade_id])
            else:
                cursor.execute("""
                    SELECT a.aco_codigo, a.aco_descricao
                    FROM areacomercial a ORDER BY aco_descricao
                """)

            resultados = cursor.fetchall()

        associacoes = [
            {'aco_codigo': row[0], 'aco_descricao': row[1]}
            for row in resultados
        ]

    return Response({'associacoes': associacoes})
