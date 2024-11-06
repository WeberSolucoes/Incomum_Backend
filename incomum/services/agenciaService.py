from rest_framework import status
from rest_framework.response import Response
from ..models import Agencia
from ..serializers.agenciaSerializer import AgenciaSerializer

from django.db import connection
import traceback

import base64
from django.http import JsonResponse, Http404
from django.shortcuts import get_object_or_404

def find_by_id(id):
    entity = Agencia.objects.get(age_codigo=id)
    return Response(AgenciaSerializer(entity).data, status=status.HTTP_200_OK)

def list_all():
    entities = Agencia.objects.all()
    return Response(AgenciaSerializer(entities, many=True).data, status=status.HTTP_200_OK)

def create(request):
    serializer = AgenciaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def update(request, id):
    try:
        agencia: Agencia = Agencia.objects.get(age_codigo=id)
    except Agencia.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    print("Dados recebidos para atualização:", request.data)
    serializer = AgenciaSerializer(agencia, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def delete(id):
    try:
        agencia: Agencia = Agencia.objects.get(age_codigo=id)
    except Agencia.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    agencia.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


def update_logo(request, id):
    try:
        agencia = Agencia.objects.get(age_codigo=id)
    except Agencia.DoesNotExist:
        return Response({"error": "Agência não encontrada"}, status=status.HTTP_404_NOT_FOUND)

    if 'age_imagem' in request.FILES:
        file = request.FILES['age_imagem']

        try:
            # Lê os dados da imagem como binário
            file_data = file.read()

            # Atualiza o campo age_imagem (tipo bytea)
            agencia.age_imagem = file_data
            agencia.save()

            return Response({"message": "Imagem atualizada com sucesso"}, status=status.HTTP_200_OK)

        except Exception as e:
            print("Erro ao atualizar a imagem:", traceback.format_exc())
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    else:
        return Response({"error": "Nenhuma imagem foi fornecida"}, status=status.HTTP_400_BAD_REQUEST)

def get_agencia_imagem(request, id):
    agencia = get_object_or_404(Agencia, age_codigo=id)

    if not agencia.age_imagem:
        raise Http404("Imagem não encontrada")

    try:
        image_data = base64.b64encode(agencia.age_imagem).decode('utf-8')
        response_data = {"image": f"data:image/png;base64,{image_data}"}
        print(response_data)  # Adicione este log
        return JsonResponse(response_data, status=200)
    except Exception as e:
        print("Erro ao retornar a imagem:", e)
        raise Http404("Erro ao retornar a imagem.")
