from rest_framework import status
from rest_framework.response import Response
from ..models.agente import Agente
from ..serializers.agenteSerializer import AgenteSerializer
from django.http import JsonResponse


def find_by_id(id):
    entity = Agente.objects.get(agt_codigo=id)
    return Response(AgenteSerializer(entity).data, status=status.HTTP_200_OK)

def list_all():
    entities = Agente.objects.all().order_by('agt_descricao')
    return Response(AgenteSerializer(entities, many=True).data, status=status.HTTP_200_OK)

def create(request):
    serializer = AgenteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def update(request, id):
    try:
        agente: Agente = Agente.objects.get(agt_codigo=id)
    except Agente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = AgenteSerializer(agente, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def delete(id):
    try:
        agente: Agente = Agente.objects.get(agt_codigo=id)
    except Agente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    agente.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

def get_agentes_por_agencia(request, age_codigo):
    agentes = Agente.objects.filter(age_codigo=age_codigo).values(
        'agt_codigo', 
        'agt_descricao', 
        'agt_cpf', 
        'agt_email',
        'agt_cep', 
        'agt_endereco', 
        'agt_numero', 
        'agt_bairro', 
        'cid_codigo', 
        'agt_fone', 
        'agt_celular', 
        'agt_comissao', 
        'ban_codigo', 
        'agt_agencia', 
        'agt_contacorrente', 
        'age_codigo'  # Inclua age_codigo aqui se necessário
    )
    return JsonResponse(list(agentes), safe=False)
