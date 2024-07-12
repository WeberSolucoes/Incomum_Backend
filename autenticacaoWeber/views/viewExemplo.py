from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from ..models.modelExemplo import Tarefa
from ..serializers.serializerExemplo import *
from drf_yasg.utils import swagger_auto_schema

from ..services import serviceExemplo


@swagger_auto_schema(
    method='get',
    responses={status.HTTP_201_CREATED: myModelSaveDto},
    tags=['Tarefa']
)
@api_view(['GET'])
def get(request, id):
    try:
        entity: Tarefa = Tarefa.objects.get(id=id)
        response = myModelSaveDto(entity)
        return Response(response.data, status=status.HTTP_200_OK)
    except Tarefa.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@swagger_auto_schema(
    method='post',
    request_body=myModelUpdateDto,
    responses={status.HTTP_201_CREATED: myModelSaveDto},
    tags=['Tarefa']
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post(request):
    request = myModelUpdateDto(data=request.data)
    if request.is_valid():
        entity: Tarefa = Tarefa.objects.create(**request.validated_data)
        response = myModelSaveDto(entity)
        return Response(response.data, status=status.HTTP_201_CREATED)
    return Response(request.errors, status=status.HTTP_400_BAD_REQUEST)
    
@swagger_auto_schema(
    method='put',
    request_body=myModelUpdateDto,
    responses={status.HTTP_201_CREATED: myModelUpdateDto},
    tags=['Tarefa']
)
@api_view(['PUT'])
def put(request,id):
    request = myModelUpdateDto(data=request.data)
    if request.is_valid():
        if(request.validated_data.get('nome') is None and request.validated_data.get('concluida') is None and request.validated_data.get('created') is None):
            return Response(request.errors, status=status.HTTP_400_BAD_REQUEST)
        entity: Tarefa = Tarefa.objects.get(id=id)
        entity.nome = request.validated_data.get('nome') if request.validated_data.get('nome') else entity.nome
        entity.concluida = request.validated_data.get('concluida') if request.validated_data.get('concluida') is not None else entity.concluida
        entity.created = request.validated_data.get('created') if request.validated_data.get('created') else entity.created
        entity.save()
        response = myModelUpdateDto(entity)
        return Response(response.data, status=status.HTTP_201_CREATED)
    return Response(request.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='delete',
    responses={status.HTTP_200_OK: "Entidade Deletada"},
    tags=['Tarefa']
)
@api_view(['DELETE'])
def delete(request, id):
    entity: Tarefa = Tarefa.objects.get(id=id)
    entity.delete()
    return Response("Entidade Deletada", status=status.HTTP_200_OK)

@swagger_auto_schema(
    method='get',
    responses={status.HTTP_200_OK: MeuModeloSerializer(many=True)},
    tags=['Tarefa']
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAll(request):
    entities = Tarefa.objects.all()
    response = MeuModeloSerializer(entities, many=True)
    return Response(response.data, status=status.HTTP_200_OK)

@swagger_auto_schema(
    method='get',
    responses={status.HTTP_200_OK: UserSerializer()},
    tags=['Details']
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def userDetails(request: Request)-> Response:
    #If para tratar erros de request
    try:
        return serviceExemplo.userDetailsService(request)
    except User.DoesNotExist as e:
        print(e)
        return Response(status=status.HTTP_404_NOT_FOUND,)
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,)
