import datetime
import io
import json
from turtle import pd
from django.http import HttpResponse
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
    user_unidades = [id['loj_codigo'] for id in user_unidades]
    
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

    relatorios = Relatorio.objects.filter(
        fim_data__range=[data_inicio, data_fim]
    ).filter(loj_codigo__in=user_unidades).values("fim_valorliquido", "fim_valorinc", "fim_valorincajustado")
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
    totais["total_valorliquido"] = locale.currency(totais["total_valorliquido"], grouping=True)
    totais["total_valorinc"] = locale.currency(totais["total_valorinc"], grouping=True)
    totais["total_valorincajustado"] = locale.currency(totais["total_valorincajustado"], grouping=True)
    print(totais)
    return Response(totais,status=status.HTTP_200_OK)


def list_all_byfilter(request) -> Response:
    data_inicio = request.query_params.get("dataInicio")
    data_fim = request.query_params.get("dataFim")
    export = request.query_params.get("export", "false")

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

    if export == "true":
        serializer = RelatorioSerializer(relatorios, many=True)
        return Response(serializer.data)

    paginator = PageNumberPagination()
    paginator.page_size = request.query_params.get("pageSize", 10)
    paginated_relatorios = paginator.paginate_queryset(relatorios, request)
    serializer = RelatorioSerializer(paginated_relatorios, many=True)
    return paginator.get_paginated_response(serializer.data)


def total_byfilter(request) -> Response:
    data_inicio = request.query_params.get("dataInicio")
    data_fim = request.query_params.get("dataFim")

    usuario_id = request.query_params.get("usuario_id")
    user_unidades = list_all_lojas_byfilter(usuario_id).data
    user_unidades = [id['loj_codigo'] for id in user_unidades]
    
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

    relatorios = Relatorio.objects.filter(
        fim_data__range=[data_inicio, data_fim]
    ).filter(loj_codigo__in=user_unidades).values("fim_valorliquido", "fim_valorinc", "fim_valorincajustado")
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
    totais["total_valorliquido"] = locale.currency(totais["total_valorliquido"], grouping=True)
    totais["total_valorinc"] = locale.currency(totais["total_valorinc"], grouping=True)
    totais["total_valorincajustado"] = locale.currency(totais["total_valorincajustado"], grouping=True)
    print(totais)
    return Response(totais,status=status.HTTP_200_OK)


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

def list_all_areas(request) -> Response:
    areas = AreaComercial.objects.all().values("aco_codigo", "aco_descricao")
    return Response(list(areas))