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

    # Construindo a query base com o ORM do Django
    queryset = Relatorio.objects.filter(
        fim_data__range=(data_consulta_dt, data_consulta_final_dt)
    ).values(
        'fim_tipo',
        'tur_numerovenda',
        'tur_codigo',
        'fim_data',
        'fim_markup',
        'fim_valorinc',
        'fim_valorincajustado',
        'fim_valorliquido',
        'aco_descricao',
        'age_descricao',
        'ven_descricao'
    )

    # Aplicando filtros adicionais
    if user_areas:
        queryset = queryset.filter(aco_codigo__in=user_areas)

    if unidade_selecionada:
        queryset = queryset.filter(loj_codigo=unidade_selecionada)

    if areas_selecionadas:
        queryset = queryset.filter(aco_codigo__in=areas_selecionadas)

    if agencia_selecionada:
        queryset = queryset.filter(age_codigo=agencia_selecionada)

    if vendedor_selecionada:
        queryset = queryset.filter(ven_codigo=vendedor_selecionada)

    # Ordenando os resultados pela data
    queryset = queryset.order_by('fim_data')

    # Paginação
    paginator = Paginator(queryset, 100000)  # 100 resultados por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Formatando os resultados com o serializer
    resultados_formatados = [RelatorioSerializer(resultado).data for resultado in page_obj]

    # Calculando as somas após aplicar os filtros
    soma_totais = queryset.aggregate(
        total_valorinc=Sum('fim_valorinc'),
        total_valorincajustado=Sum('fim_valorincajustado'),
        total_valorliquido=Sum('fim_valorliquido'),
    )

    return Response({
        'resultados': resultados_formatados,
        'num_paginas': paginator.num_pages,
        'pagina_atual': page_obj.number,
        'has_next': page_obj.has_next(),
        'has_previous': page_obj.has_previous(),
        'soma_totais': {
            'total_valorinc': soma_totais.get('total_valorinc', 0),
            'total_valorincajustado': soma_totais.get('total_valorincajustado', 0),
            'total_valorliquido': soma_totais.get('total_valorliquido', 0),
        }
    }, status=status.HTTP_200_OK)


def list_all_lojas_byfilter(request):
    # Filtrar as lojas conforme necessário, por exemplo:
    # lojas = Loja.objects.filter(user=request.user)
    lojas = Loja.objects.all()  # Obtém todas as lojas

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
    user_id = request.user.id  # Obtém o ID do usuário logado

    # Obtém os aco_codigo associados ao usuário logado
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT ac.aco_codigo
            FROM usuariocomercial ac
            INNER JOIN auth_user uac ON uac.id = ac.usr_codigo
            WHERE uac.id = %s
        """, [user_id])
        user_areas = [row[0] for row in cursor.fetchall()]

    if not user_areas:
        # Se não houver aco_codigo, retornamos todos os vendedores
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT v.ven_codigo, v.ven_descricao
                FROM vendedor v
                ORDER BY v.ven_descricao
            """)
            vendedores = cursor.fetchall()
    else:
        # Consulta os vendedores baseados na aco_codigo do usuário
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT DISTINCT v.ven_codigo, v.ven_descricao
                FROM faturamentosimplificado f
                JOIN vendedor v ON v.ven_codigo = f.ven_codigo
                WHERE f.aco_codigo IN %s
                ORDER BY v.ven_descricao
            """, [tuple(user_areas)])
            vendedores = cursor.fetchall()

    vendedores_formatados = [{
        'ven_codigo': ven[0],
        'ven_descricao': ven[1]
    } for ven in vendedores]

    return Response({'vende': vendedores_formatados})



def list_all_agencias_byfilter(request) -> Response:
    user_id = request.user.id  # Obtém o ID do usuário logado

    # Obter o aco_codigo associado ao usuário
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT ac.aco_codigo
            FROM usuariocomercial ac
            INNER JOIN auth_user uac ON uac.id = ac.usr_codigo
            WHERE uac.id = %s
        """, [user_id])
        user_aco_codigos = [row[0] for row in cursor.fetchall()]

    if user_aco_codigos:
        # Buscar as agências associadas ao(s) aco_codigo do usuário
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT a.age_codigo, a.age_descricao
                FROM agencia a
                WHERE a.aco_codigo IN %s
            """, [tuple(user_aco_codigos)])
            resultados = cursor.fetchall()
    else:
        # Se não houver aco_codigo, retornar todas as agências
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT a.age_codigo, a.age_descricao
                FROM agencia a
                ORDER BY a.age_descricao
            """)
            resultados = cursor.fetchall()

    # Formatar os resultados como uma lista de dicionários
    valores = [
        {'age_codigo': row[0], 'age_descricao': row[1]}
        for row in resultados
    ]

    return Response({'valores': valores}, status=status.HTTP_200_OK)




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
        'Income',
        'Income Ajustado',
        'Descrição Área Comercial',
        'Descrição Agência',
        'Descrição Vendedor',
        'Valor Venda Bruta'
    ]
    ws.append(headers)

    total_valor_liquido = 0
    total_income = 0
    total_income_ajustado = 0
    total_valor_venda_bruta = 0

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

        # Acumulando os totais
        total_valor_liquido += relatorio['fim_valorliquido']
        total_income += relatorio['fim_valorinc']
        total_income_ajustado += relatorio['fim_valorincajustado']
        total_valor_venda_bruta += relatorio['fat_valorvendabruta']

    # Adicionando a linha de totais
    ws.append([
        'Totais',
        '',
        '',
        locale.currency(total_valor_liquido, grouping=True),
        '',
        '',
        locale.currency(total_income, grouping=True),
        locale.currency(total_income_ajustado, grouping=True),
        '',
        '',
        '',
        locale.currency(total_valor_venda_bruta, grouping=True),
    ])

    buffer = io.BytesIO()
    wb.save(buffer)
    buffer.seek(0)
    return buffer.getvalue()



def list_all_areas(request) -> Response:
    areas = AreaComercial.objects.all()
    return Response(list(areas))
