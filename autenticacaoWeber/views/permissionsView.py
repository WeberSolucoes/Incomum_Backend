from ..serializers.permissionSerializer import PermissionSerializer, PermissionByGroupSerializer, UserPermissionsDTOSerializer, UserPermissionsUpdateDTOSerializer
from typing import List
# views.py
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.contrib.auth.models import Permission, Group
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from ..models.usuario import Usuario as User
@swagger_auto_schema(
        method='get',
        responses={200: PermissionSerializer(many=True)},
        tags=['Permissoes'])
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
def permission_list(request):
    permissions = Permission.objects.all()
    serializer = PermissionSerializer(permissions, many=True)
    return Response(serializer.data)

@swagger_auto_schema(
        method='post', 
        request_body=PermissionSerializer, 
        responses={201: PermissionSerializer},
        tags=['Permissoes'])
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
def permission_create(request):
    serializer = PermissionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
        method='get',
        responses={200: PermissionSerializer},
        tags=['Permissoes'])
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
def permission_detail(request, pk):
    try:
        permission = Permission.objects.get(pk=pk)
    except Permission.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = PermissionSerializer(permission)
    return Response(serializer.data)

@swagger_auto_schema(method='put',
                    request_body=PermissionSerializer,
                    responses={200: PermissionSerializer},
                    tags=['Permissoes'])
@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
def permission_update(request, pk):
    try:
        permission = Permission.objects.get(pk=pk)
    except Permission.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = PermissionSerializer(permission, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
        method='delete', 
        responses={204: openapi.Response(description="No Content")},
        tags=['Permissoes'])
@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
def permission_delete(request, pk):
    try:
        permission = Permission.objects.get(pk=pk)
    except Permission.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    permission.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@swagger_auto_schema(
        method='post',
        request_body= PermissionByGroupSerializer,
        responses={200: PermissionSerializer(many=True)},
        tags=['Permissoes'])
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
def permission_list_by_groups(request):
    serializer = PermissionByGroupSerializer(data=request.data)
    if serializer.is_valid():
        groups: List[Group] = Group.objects.filter(id__in=request.data.get('ids'))
        groupsid = set(groups.values_list('id', flat=True))
        ids_invalidos = [id for id in request.data.get('ids') if id not in groupsid]
        if ids_invalidos:
            return Response({'message': 'Algum ou Alguns Grupos são inválidos'} ,status=status.HTTP_412_PRECONDITION_FAILED)
        permissions = Permission.objects.filter(group__in=groups)
        serializer = PermissionSerializer(permissions, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
@swagger_auto_schema(
    methods=['get'],
    responses={200: UserPermissionsDTOSerializer(many=True)},
    tags=['Permissoes']
)
@api_view(['GET'])
def list_permissions(request, id):
    try:
        user: User = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    permissions = user.user_permissions.all()
    serializer = UserPermissionsDTOSerializer(permissions, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(
    methods=['post'],
    request_body= UserPermissionsUpdateDTOSerializer,
    responses={200: UserPermissionsDTOSerializer(many=True)},
    tags=['Permissoes']
)
@api_view(['POST'])
def update_permissions(request, id):
    try:
        user: User = User.objects.get(id=id)
        permissions: List[Permission] = Permission.objects.filter(id__in=request.data.get('permissionsId'))
        permissions_ids = set(permissions.values_list('id', flat=True))
        ids_invalidos = [id for id in request.data.get('permissionsId') if id not in permissions_ids]
        if ids_invalidos:
            return Response({'message': 'Alguma ou Algumas Permissoes são inválidas'} ,status=status.HTTP_412_PRECONDITION_FAILED)
    except User.DoesNotExist:
        return Response({'message': 'Usuário não encontrado'} ,status=status.HTTP_404_NOT_FOUND)

    serializer = UserPermissionsUpdateDTOSerializer(data=request.data)
    if serializer.is_valid():
        permissions = serializer.validated_data.get('permissionsId')
        user.user_permissions.set(permissions)
        user.save()
        serializer = UserPermissionsDTOSerializer(user.user_permissions.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)