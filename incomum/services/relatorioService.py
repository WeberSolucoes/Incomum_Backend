
from django.db import connection
from rest_framework.response import Response
from rest_framework import status

from autenticacaoWeber.models.usuario import *
from incomum.serializers.vendedorSerializer import VendedorSerializer
from incomum.serializers import agenciaSerializer

from ..models import *
from ..serializers.relatorioSerializer import *

def findById(id) -> Response:
    try:
        relatorio: FaturamentoSimplificado = FaturamentoSimplificado.objects.get(loj_codigo = id)
    except FaturamentoSimplificado.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = relatorioSerializer(relatorio)
    return Response(serializer.data)

def create(request) -> Response:
    serializer = relatorioSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def update(request, id) -> Response:
    try:
        loja: FaturamentoSimplificado = FaturamentoSimplificado.objects.get(loj_codigo = id)
    except FaturamentoSimplificado.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = relatorioSerializer(loja, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def delete(id) -> Response:
    try:
        loja: FaturamentoSimplificado = FaturamentoSimplificado.objects.get(loj_codigo = id)
    except FaturamentoSimplificado.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    loja.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

def list_all(request):

    # Obtém os parâmetros da consulta
    date_start = request.query_params.get('dateStart')
    date_end = request.query_params.get('dateEnd')


    # Adiciona a filtragem por data e aco_codigo
    if date_start and date_end:
        try:
            data = FaturamentoSimplificado.objects.filter(
                fim_data__range=[date_start, date_end]
            ).select_related('loj_codigo', 'aco_codigo')
        except ValueError:
            return Response({"detail": "Invalid date format"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        data = FaturamentoSimplificado.objects.filter(
        ).select_related('loj_codigo', 'aco_codigo')

    serializer = relatorioSerializer(data, many=True)
    # Retorna também as áreas comerciais
    return Response({
        'data': serializer.data
    })

def filtraunidade(request):
    # Obtém o ID do usuário
    user_id = request.user.id
    
    # Consulta os aco_codigo associados ao usuário
    user_aco_codes = UsuarioAreaComercial.objects.filter(usuario_id=user_id).values_list('area_comercial_id', flat=True)
    
    # Filtra as áreas comerciais com base nos códigos obtidos
    areas = AreaComercial.objects.filter(aco_codigo__in=user_aco_codes)
    areas_list = [{'aco_codigo': area.aco_codigo, 'aco_descricao': area.aco_descricao} for area in areas]
    
    return Response({
        'areas_comerciais': areas_list
    })

def filtra_vendedores(request):
    user_id = request.user.id
    
    # Passo 1: Obtém as áreas comerciais associadas ao usuário
    user_areas = UsuarioAreaComercial.objects.filter(usuario_id=user_id).values_list('area_comercial_id', flat=True)
    areas_user = UsuarioAreaComercial.objects.filter(usuario_id=user_id).values_list('usuario_id', flat=True)
    
    # Passo 2: Obtém as lojas associadas às áreas comerciais
    lojas = Loja.objects.filter(aco_codigo__in=user_areas).distinct()
    
    # Passo 3: Filtra os vendedores baseando-se nas lojas obtidas
    vendedores = Vendedor.objects.filter(
        usr_codigo= user_id
    )
    if vendedores is None:
        vendedores = Vendedor.objects.filter(
            usr_codigo__in=areas_user
        )
    
    # Serializa os dados
    vendedores_list = [{'ven_codigo': vendedor.ven_codigo, 'ven_descricaoweb1': vendedor.ven_descricaoweb1} for vendedor in vendedores]
    print(vendedores_list)

    return Response({
        'vendedores': vendedores_list
    })


def filtra_agencia(request, id):
    try:
        # Filtra as agências com base no ID
        consulta = Agencia.objects.filter(aco_codigo=id)
        if consulta.exists():
            # Serializa os dados
            serializer = agenciaSerializer.AgenciaSerializer(consulta, many=True)
            return Response({
                'consulta': serializer.data  # Retorna os dados serializados
            })
        else:
            return Response({'Obs': 'Nenhum Registro Encontrado'}, status=status.HTTP_404_NOT_FOUND)
    except Agencia.DoesNotExist:
        return Response({'Obs': 'Agencia não Encontrada'}, status=status.HTTP_404_NOT_FOUND)