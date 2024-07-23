# views.py
from typing import List
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.contrib.auth.models import Group, Permission	
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from ..serializers.permissionSerializer import GroupSerializer, GroupResponseSerializer, UserGruposDTOSerializer, UserGruposUpdateDTOSerializer
from ..models.usuario import Usuario as User
 
@swagger_auto_schema(
        method='get',
        responses={200: GroupSerializer(many=True)},
        tags=['Grupos'])
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
def group_list(request):
    groups = Group.objects.all()
    serializer = GroupResponseSerializer(groups, many=True)
    return Response(serializer.data)

@swagger_auto_schema(
        method='post', 
        request_body=GroupSerializer, 
        responses={201: GroupSerializer},
        tags=['Grupos'])
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
def group_create(request):
    serializer = GroupSerializer(data=request.data)
    if serializer.is_valid():
        if len(serializer.validated_data['permissions']) == 0:
            return Response({"message":"O grupo precisa ter pelo menos uma permissão"} ,status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
        method='get', 
        responses={200: GroupSerializer},
        tags=['Grupos'])
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
def group_detail(request, pk):
    try:
        group = Group.objects.get(pk=pk)
    except Group.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = GroupResponseSerializer(group)
    return Response(serializer.data)

@swagger_auto_schema(
        method='put', 
        request_body=GroupSerializer, 
        responses={200: GroupSerializer},
        tags=['Grupos'])
@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
def group_update(request, pk):
    try:
        group = Group.objects.get(pk=pk)
    except Group.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = GroupSerializer(group, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
        method='delete', 
        responses={204: openapi.Response(description="No Content")},
        tags=['Grupos'])
@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
def group_delete(request, pk):
    try:
        group = Group.objects.get(pk=pk)
    except Group.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    group.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@swagger_auto_schema(
    methods=['get'],
    responses={200: UserGruposDTOSerializer(many=True)},
    tags=['Grupos']
)
@api_view(['GET'])
def list_groups(request, id):
    try:
        user: User = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    grupos = user.groups.all()
    serializer = UserGruposDTOSerializer(grupos, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@swagger_auto_schema(
    methods=['post'],
    request_body= UserGruposUpdateDTOSerializer,
    responses={200: UserGruposDTOSerializer(many=True)},
    tags=['Grupos']
)
@api_view(['POST'])
def update_groups(request, id):
    try:
        user: User = User.objects.get(id=id)
        grupos: List[Group] = Group.objects.filter(id__in=request.data.get('gruposId'))
        grupos_ids = set(grupos.values_list('id', flat=True))
        ids_invalidos = [id for id in request.data.get('gruposId') if id not in grupos_ids]
        if ids_invalidos:
            return Response({'message': 'Algum ou Alguns Grupos são inválidos'} ,status=status.HTTP_412_PRECONDITION_FAILED)
    except User.DoesNotExist:
        return Response({'message': 'Usuário não encontrado'} ,status=status.HTTP_404_NOT_FOUND)

    serializer = UserGruposUpdateDTOSerializer(data=request.data)
    if serializer.is_valid():
        grupos = serializer.validated_data.get('gruposId')
        print(grupos)
        user.groups.set(grupos)
        user.save()

        gruposUsuario = user.groups.all()
        permissoes = []
        for grupo in gruposUsuario:
            permissao = Permission.objects.filter(group=grupo)
            permissoes.extend(permissao)
        user.user_permissions.set(permissoes)
        user.save()
        
        serializer = UserGruposDTOSerializer(user.groups.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

