
import datetime
from rest_framework.response import Response
from rest_framework import status

from autenticacaoWeber.models.usuario import *
from incomum.serializers.vendedorSerializer import VendedorSerializer
from incomum.serializers import agenciaSerializer

from ..models import *
from ..serializers.relatorioSerializer import *

def list_all_byfilter(request)->Response:
    data_inicio = request.query_params.get('dataInicio')
    data_fim = request.query_params.get('dataFim')

    if data_inicio == None or data_fim == None:
        return Response({'message': 'Os parâmetros data inicial e data final são obrigatórios.'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        data_inicio = datetime.datetime.strptime(data_inicio, '%d-%m-%Y')
        data_fim = datetime.datetime.strptime(data_fim, '%d-%m-%Y')
        if data_fim < data_inicio:
            return Response({'message': 'A data final deve ser maior que a data inicial.'}, status=status.HTTP_400_BAD_REQUEST)

    except ValueError:
        return Response({'message': 'Data inválida. Use o formato YYYY-MM-DD.'}, status=status.HTTP_400_BAD_REQUEST)
    
    unidades = request.query_params.getlist('unidade')
    areaComerciais = request.query_params.getlist('areaComercial')
    agencias = request.query_params.getlist('agencia')
    vendedores = request.query_params.getlist('vendedor')

    relatorios = Relatorio.objects.filter(fim_data__range=[data_inicio, data_fim])

    if len(unidades) > 0:
        relatorios = relatorios.filter(loj_codigo__in = unidades)

    if len(areaComerciais) > 0 :
        relatorios = relatorios.filter(aco_codigo__in = areaComerciais)

    if len(agencias) > 0 :
        relatorios = relatorios.filter(age_codigo__in = agencias)

    if len(vendedores) > 0 :
        relatorios = relatorios.filter(ven_codigo__in = vendedores)
    relatorios = relatorios[:100]
    serializer = RelatorioSerializer(relatorios, many=True)

    return Response(serializer.data)
    
def list_all_lojas_byfilter(id)->Response:
    areasId = AreaComercial.objects.filter(usuarioareacomercial__usuario_id = id)
    lojas_id = set(areasId.values_list('loja_codigo',flat=True))
    lojas = Loja.objects.filter(loj_codigo__in = lojas_id).values('loj_codigo', 'loj_descricao')

    return Response(lojas)

def list_all_areas_byfilter(request ,id)->Response:
    areas = AreaComercial.objects.filter(usuarioareacomercial__usuario_id = id).values('aco_codigo', 'aco_descricao')
    unidades = request.query_params.getlist('unidade')

    if len(unidades) > 0:
        areas = areas.filter(loja_codigo__in = unidades)

    return Response(areas)

def list_all_vendedores_byfilter(request ,id)->Response:
    user = Usuario.objects.get(id = id)
    if (user.groups.filter(name = 'Vendedor').exists()):
        data = {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name
        }
        return Response(data=data)
    else:
        unidades = request.query_params.getlist('unidade')
        print(unidades)
        if len(unidades) == 0:
            return Response({'message': 'O parâmetro unidade é obrigatório.'}, status=status.HTTP_400_BAD_REQUEST)
        #procuro as areas comercias filtrando pela unidade
        #acho os usuarios pela area comercial
        #verifico quais usuario sao vendedores e voalá
        areas = AreaComercial.objects.filter(loja_codigo__in = unidades)
        usuarios = UsuarioAreaComercial.objects.filter(area_comercial__in = areas)
        usuarios = Usuario.objects.filter(id__in = usuarios.values_list('usuario_id', flat=True))
        vendedores = usuarios.filter(groups__name = 'Vendedor').values('id', 'first_name', 'last_name')

        return Response(vendedores)

def list_all_agencias_byfilter(request ,id)->Response:
    areas = AreaComercial.objects.filter(usuarioareacomercial__usuario_id = id).values_list('aco_codigo', flat=True)
    agencias = Agencia.objects.filter(aco_codigo__in = areas).values('age_codigo', 'age_descricao')

    areasComerciais = request.query_params.getlist('areaComercial')

    if len(areasComerciais) > 0:
        agencias = agencias.filter(aco_codigo__in = areasComerciais)

    return Response(agencias)
