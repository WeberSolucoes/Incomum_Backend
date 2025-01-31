from rest_framework.response import Response
from rest_framework import status
from ..models import *
from ..serializers.cidadeSerializer import *

def findById(id) -> Response:
    try:
        loja: Loja = Cidade.objects.get(cid_codigo = id)
    except Cidade.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CidadeSerializer(loja)
    return Response(serializer.data)

def create(request) -> Response:
    serializer = CidadeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def update(request, id) -> Response:
    try:
        loja: Loja = Cidade.objects.get(cid_codigo = id)
    except Cidade.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CidadeSerializer(loja, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def delete(id) -> Response:
    try:
        loja: Loja = Cidade.objects.get(cid_codigo = id)
    except Cidade.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    loja.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

def list_all() -> Response:
    lojas = Cidade.objects.all()
    serializer = CidadeSerializer(lojas, many=True)
    return Response(serializer.data)


from django.db import connection

from django.db import connection

def search_cidades(request):
    query = request.GET.get('q', '').strip()
    print(f"Consultando por: {query}")
    
    if len(query) >= 3:
        with connection.cursor() as cursor:
            sql_query = """
                SELECT cid_codigo, cid_descricao, cid_estado, reg_codigo, cid_pais, cid_sigla, pai_codigo
                FROM cidade
                WHERE LOWER(TRIM(cid_descricao)) LIKE LOWER(%s)
            """
            parametro = f'%{query}%'
            
            cursor.execute(sql_query, [parametro])
            cidades = cursor.fetchall()
            
            cidade_list = [{'label': cidade[1], 'value': cidade[0]} for cidade in cidades]
            return Response(cidade_list, status=status.HTTP_200_OK)
    else:
        return Response([], status=status.HTTP_200_OK)
