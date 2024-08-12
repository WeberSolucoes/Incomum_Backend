from rest_framework.response import Response
from rest_framework import status
from typing import List

from django.db.utils import IntegrityError
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import Group, Permission
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str

from ..models.usuario import Usuario as User 
from ..serializers.usuarioSerializer import UsuarioDTOSerializer
from ..mappers.usuarioMapper import *

def findById(id) -> Response:
    try:
        user: User = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = EntityToDto(user)
    return Response(serializer.data, status=status.HTTP_200_OK)

def list_all() -> Response:
    users = User.objects.all()
    serializer = EntitiesToDtos(users)
    return Response(serializer.data, status=status.HTTP_200_OK)

def create(request) -> Response:
    serializer = UsuarioDTOSerializer(data=request.data)
    if serializer.is_valid():
        user: Usuario = DtoToEntity(serializer)
        senha = user.first_name[0] + '@' + user.usr_cpf
        user.set_password(senha)
        try:
            user.save()
        except IntegrityError as e:
            return Response(status=status.HTTP_409_CONFLICT)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def update(request, id) -> Response:
    try:
        user: User = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UsuarioDTOSerializer(data=request.data)
    if serializer.is_valid():
        DtoToEntityUpdate(serializer, user)
        user.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def delete(id) -> Response:
    try:
        user: User = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

def update_password(request) -> Response:
    serializer = EmailSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data.get('email')
        try:
            user: User = User.objects.get(email=email)
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            host = request.get_host()
            reset_link = request.build_absolute_uri(
                f'{host}/redefinir-senha/{uid}/{token}/'
            )
            message = f"""
            <p>Ola {user.username},</p>
            <p>Você esta recebendo este email porque solicitou uma alteração de senha para sua conta no nosso site.</p>
            <p>Por favor, acesse a seguinte página e escolha uma nova senha:</p>
            <p><a href="{reset_link}">{reset_link}</a></p>
            <p>Se você não solicitou esta alteração, ignore este email.</p>
            <p>Obrigado por utilizar nosso site!</p>
            """
            send_mail(
                'Requisitação de Alteração de Senha',
                '',
                'suporte@webersolucoes.com.br',
                [email],
                fail_silently=False,
                html_message=message
            )
            return Response( {'message': 'Email enviado'} ,status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'message': 'Email não encontrado'} ,status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def update_password_confirm(request, uidb64, token) -> Response:
    serializer = PasswordSerializer(data=request.data)
    if serializer.is_valid():
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
            if default_token_generator.check_token(user, token):
                user.set_password(serializer.validated_data.get('new_password'))
                user.save()
                return Response({'message': 'Senha alterada com sucesso'} ,status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Token inválido ou expirado'} ,status=status.HTTP_400_BAD_REQUEST)
        except(TypeError,ValueError,OverflowError,User.DoesNotExist):
            return Response({'message': 'Token inválido ou expirado'} ,status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)