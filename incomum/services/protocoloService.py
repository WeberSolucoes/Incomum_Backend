from rest_framework.response import Response
from rest_framework import status
from ..models import *
from ..serializers.protocoloSerializer import *

def findById(id) -> Response:
    try:
        loja: Loja = Protocolo.objects.get(prt_codigo = id)
    except Protocolo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ProtocoloSerializer(loja)
    return Response(serializer.data)

def create(request) -> Response:
    serializer = ProtocoloSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def update(request, id) -> Response:
    try:
        loja: Loja = Protocolo.objects.get(prt_codigo = id)
    except Protocolo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ProtocoloSerializer(loja, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def delete(id) -> Response:
    try:
        loja: Loja = Protocolo.objects.get(prt_codigo = id)
    except Protocolo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    loja.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

def list_all() -> Response:
    lojas = Protocolo.objects.all()
    serializer = ProtocoloSerializer(lojas, many=True)
    return Response(serializer.data)


from rest_framework.response import Response
from django.db.models import Subquery, OuterRef
from incomum.models.parceiro import Parceiro
from incomum.models.protocolo import Protocolo
from incomum.models.centroCusto import CentroCusto
from incomum.models.loja import Loja
from incomum.models.moeda import Moeda
from incomum.serializers import protocoloSerializer
from django.utils import timezone
from django.shortcuts import get_list_or_404

def relatorio(request) -> Response:
    # Extrair os parâmetros de filtro da requisição
    date_start = request.GET.get('dateStart')  # Data inicial (yyyy-mm-dd)
    date_end = request.GET.get('dateEnd')  # Data final (yyyy-mm-dd)
    pagamentoStart = request.GET.get('pagamentoStart')  # Data inicial (yyyy-mm-dd)
    pagamentoEnd = request.GET.get('pagamentoEnd')  # Data final (yyyy-mm-dd)
    unidade = request.GET.get('unidade')  # Unidade selecionada
    area_comercial = request.GET.getlist('areaComercial')  # Áreas comerciais selecionadas (lista)
    protocolo = request.GET.get('protocolo')  # Número do protocolo
    conta_bancaria = request.GET.getlist('contaBancaria')  # Contas bancárias selecionadas (lista)
    situacao_protocolo = request.GET.getlist('situacaoProtocolo')  # Situações do protocolo (lista)
    centro_custo = request.GET.getlist('centroCusto')  # Centros de custo selecionados (lista)
    moe_codigo = request.GET.get('moe_codigo')  # Código da moeda selecionada

    # Log dos filtros recebidos
    print("Filtros recebidos no backend:")
    print("dateStart:", date_start)
    print("dateEnd:", date_end)
    print("unidade:", unidade)
    print("areaComercial:", area_comercial)
    print("protocolo:", protocolo)
    print("contaBancaria:", conta_bancaria)
    print("situacaoProtocolo:", situacao_protocolo)
    print("centroCusto:", centro_custo)
    print("moe_codigo:", moe_codigo)

    # Iniciar a query com annotate
    protocolos = Protocolo.objects.annotate(
        loja_nome=Subquery(
            Loja.objects.filter(loj_codigo=OuterRef('loj_codigo')).values('loj_descricao')[:1]
        ),
        conta_nome=Subquery(
            CentroCusto.objects.filter(cta_codigo=OuterRef('cta_codigo')).values('cta_descricao')[:1]
        ),
        fornecedor_nome=Subquery(
            Parceiro.objects.filter(par_codigo=OuterRef('par_codigo')).values('par_descricao')[:1]
        )
    ).values(
        'prt_codigo',
        'prt_datacadastro',
        'prt_datacompetencia',
        'prt_datavencimento',
        'loja_nome',
        'conta_nome',
        'fornecedor_nome',
        'prt_observacao',
        'prt_valor',
        'moe_codigo'
    )

    # Aplicar filtros
    if date_start:
        try:
            date_start = datetime.strptime(date_start, '%Y-%m-%d').date()
            date_start = timezone.make_aware(datetime.combine(date_start, datetime.min.time()))
            protocolos = protocolos.filter(prt_datacadastro__gte=date_start)
            print("date_start convertido:", date_start)
        except ValueError as e:
            print(f"Erro ao converter date_start: {e}")

    if date_end:
        try:
            date_end = datetime.strptime(date_end, '%Y-%m-%d').date()
            date_end = timezone.make_aware(datetime.combine(date_end, datetime.max.time()))
            protocolos = protocolos.filter(prt_datacadastro__lte=date_end)
            print("date_end convertido:", date_end)
        except ValueError as e:
            print(f"Erro ao converter date_end: {e}")

    if pagamentoStart:
        try:
            pagamentoStart = datetime.strptime(pagamentoStart, '%Y-%m-%d').date()
            pagamentoStart = timezone.make_aware(datetime.combine(pagamentoStart, datetime.min.time()))
            protocolos = protocolos.filter(prt_datavencimento__gte=pagamentoStart)
            print("pagamentoStart convertido:", pagamentoStart)
        except ValueError as e:
            print(f"Erro ao converter pagamentoStart: {e}")

    if pagamentoEnd:
        try:
            pagamentoEnd = datetime.strptime(pagamentoEnd, '%Y-%m-%d').date()
            pagamentoEnd = timezone.make_aware(datetime.combine(pagamentoEnd, datetime.max.time()))
            protocolos = protocolos.filter(prt_datavencimento__lte=pagamentoEnd)
            print("pagamentoEnd convertido:", pagamentoEnd)
        except ValueError as e:
            print(f"Erro ao converter pagamentoEnd: {e}")

    if unidade:
        protocolos = protocolos.filter(loj_codigo=unidade)

    if area_comercial and area_comercial != ['']:
        protocolos = protocolos.filter(aco_codigo__in=area_comercial)

    if conta_bancaria and conta_bancaria != ['']:
        protocolos = protocolos.filter(age_codigopagamento__in=conta_bancaria)

    if situacao_protocolo and situacao_protocolo != ['']:
        protocolos = protocolos.filter(prt_situacao__in=situacao_protocolo)

    if centro_custo and centro_custo != ['']:
        protocolos = protocolos.filter(cta_codigo__in=centro_custo)

    if moe_codigo:
        protocolos = protocolos.filter(moe_codigo=moe_codigo)

    if protocolo:
        protocolos = protocolos.filter(prt_codigo__icontains=protocolo)

    # Log dos resultados filtrados
    print("Resultados filtrados:", list(protocolos))  # Convertendo QuerySet para lista para visualização no log

    # Retornar os resultados como resposta
    return Response(list(protocolos))  # Convertendo QuerySet para lista




import csv
from django.http import HttpResponse
from datetime import datetime
from django.db.models import Subquery, OuterRef, Sum
import locale

def export_relatorio_csv(request):
    # Extrair os parâmetros da requisição
    date_start = request.GET.get('dateStart')
    date_end = request.GET.get('dateEnd')
    pagamentoStart = request.GET.get('pagamentoStart')
    pagamentoEnd = request.GET.get('pagamentoEnd')
    unidade = request.GET.get('unidade')
    area_comercial = request.GET.getlist('areaComercial')
    protocolo = request.GET.get('protocolo')
    conta_bancaria = request.GET.getlist('contaBancaria')
    situacao_protocolo = request.GET.getlist('situacaoProtocolo')
    centro_custo = request.GET.getlist('centroCusto')
    moe_codigo = request.GET.get('moe_codigo')

    # Criar a query com Subqueries para buscar os nomes ao invés dos IDs
    protocolos = Protocolo.objects.annotate(
        loja_nome=Subquery(
            Loja.objects.filter(loj_codigo=OuterRef('loj_codigo')).values('loj_descricao')[:1]
        ),
        conta_nome=Subquery(
            CentroCusto.objects.filter(cta_codigo=OuterRef('cta_codigo')).values('cta_descricao')[:1]
        ),
        fornecedor_nome=Subquery(
            Parceiro.objects.filter(par_codigo=OuterRef('par_codigo')).values('par_descricao')[:1]
        ),
        moeda_nome=Subquery(
            Moeda.objects.filter(moe_codigo=OuterRef('moe_codigo')).values('moe_descricao')[:1]
        )
    ).values(
        'prt_codigo', 'prt_datacadastro', 'prt_datacompetencia', 'prt_datavencimento',
        'loja_nome', 'conta_nome', 'fornecedor_nome',
        'prt_observacao', 'prt_valor', 'moeda_nome'
    )

    # Aplicar filtros se existirem
    if date_start:
        date_start = datetime.strptime(date_start, '%Y-%m-%d').date()
        protocolos = protocolos.filter(prt_datacadastro__gte=date_start)

    if date_end:
        date_end = datetime.strptime(date_end, '%Y-%m-%d').date()
        protocolos = protocolos.filter(prt_datacadastro__lte=date_end)

    if pagamentoStart:
        pagamentoStart = datetime.strptime(pagamentoStart, '%Y-%m-%d').date()
        protocolos = protocolos.filter(prt_datavencimento__gte=pagamentoStart)

    if pagamentoEnd:
        pagamentoEnd = datetime.strptime(pagamentoEnd, '%Y-%m-%d').date()
        protocolos = protocolos.filter(prt_datavencimento__lte=pagamentoEnd)

    if unidade:
        protocolos = protocolos.filter(loj_codigo=unidade)

    if area_comercial and area_comercial != ['']:
        protocolos = protocolos.filter(aco_codigo__in=area_comercial)

    if conta_bancaria and conta_bancaria != ['']:
        protocolos = protocolos.filter(age_codigopagamento__in=conta_bancaria)

    if situacao_protocolo and situacao_protocolo != ['']:
        protocolos = protocolos.filter(prt_situacao__in=situacao_protocolo)

    if centro_custo and centro_custo != ['']:
        protocolos = protocolos.filter(cta_codigo__in=centro_custo)

    if moe_codigo:
        protocolos = protocolos.filter(moe_codigo=moe_codigo)

    if protocolo:
        protocolos = protocolos.filter(prt_codigo__icontains=protocolo)

    # Calcular o total do valor
    total_valor = protocolos.aggregate(Sum('prt_valor'))['prt_valor__sum'] or 0.0

    # Criar resposta HTTP para download do CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="relatorio.csv"'

    # Criar writer do CSV
    writer = csv.writer(response, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    # Cabeçalhos do CSV
    writer.writerow([
        'Código', 'Data Cadastro', 'Data Competência', 'Data Vencimento',
        'Loja', 'Conta', 'Fornecedor', 'Observação', 'Valor', 'Moeda'
    ])

    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

    # Modificação no trecho onde escrevemos os dados no CSV
    for protocolo in protocolos:
        valor_formatado = locale.currency(protocolo['prt_valor'], grouping=True, symbol=True) if protocolo['prt_valor'] is not None else ''

        writer.writerow([
            protocolo['prt_codigo'],
            protocolo['prt_datacadastro'].strftime('%d/%m/%Y') if protocolo['prt_datacadastro'] else '',
            protocolo['prt_datacompetencia'].strftime('%d/%m/%Y') if protocolo['prt_datacompetencia'] else '',
            protocolo['prt_datavencimento'].strftime('%d/%m/%Y') if protocolo['prt_datavencimento'] else '',
            protocolo['loja_nome'] or '',  
            protocolo['conta_nome'] or '',  
            protocolo['fornecedor_nome'] or '',  
            protocolo['prt_observacao'] or '',
            valor_formatado,  # ✅ Exibir valor como "R$ 123,00"
            protocolo['moeda_nome'] or ''
        ])

    # Modificação na linha do total
    total_formatado = locale.currency(total_valor, grouping=True, symbol=True)

    writer.writerow([])
    writer.writerow(['', '', '', '', '', '', '', 'TOTAL:', total_formatado, ''])
    return response

