
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken  # Importação necessária
from ..serializers.usuarioComercialSerializer import *
from ..models.usuario_areaComercial import UsuarioAreaComercial
from django.utils.http import urlsafe_base64_decode
from django.shortcuts import get_object_or_404
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.utils.encoding import force_bytes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.http import urlsafe_base64_decode

@csrf_exempt
def login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('loginemail')
            password = data.get('loginsenha')

            # Se o usuário já está autenticado
            if request.user.is_authenticated:
                return JsonResponse({'success': True, 'message': 'Você já está logado!'})

            print(f"Tentando autenticar: email={email}, senha={password}")

            # Buscar o usuário pelo email
            try:
                usuario = User.objects.get(email=email)
            except User.DoesNotExist:
                print("Usuário não encontrado.")
                return JsonResponse({'success': False, 'error_message': 'Email ou senha inválidos.'}, status=400)

            # Verificar se a senha está correta
            if not usuario.check_password(password):
                print("Senha incorreta.")
                return JsonResponse({'success': False, 'error_message': 'Email ou senha inválidos.'}, status=400)

            # Verificar se o usuário está ativo
            if usuario.is_active:
                auth_login(request, usuario)  # Login do usuário na sessão

                # Gerar o token JWT
                refresh = RefreshToken.for_user(usuario)

                # Retornar o token de acesso e refresh
                return JsonResponse({
                    'success': True,
                    'access': str(refresh.access_token),  # Token de acesso
                    'refresh': str(refresh),  # Token de atualização (opcional)
                    'message': 'Login efetuado com sucesso!'
                })
            else:
                print("Usuário inativo.")
                return JsonResponse({'success': False, 'error_message': 'Usuário inativo.'}, status=400)

        except Exception as e:
            print(f"Erro no login: {str(e)}")
            return JsonResponse({'success': False, 'error_message': str(e)}, status=500)

    return JsonResponse({'success': False, 'error_message': 'Método não permitido'}, status=405)





def verificar_autenticacao(request):
    return JsonResponse({'authenticated': True, 'username': request.user.username})

# Caso o usuário não esteja autenticado, retorne um erro 403
def verificar_autenticacao_nao_login(request):
    return JsonResponse({'authenticated': False}, status=403)

def user_permissions_view(request):
    usuario_logado = request.user.id  # Pega o usuário logado

    # Verifica se o usuário logado existe na tabela UsuarioAreaComercial
    usuario_comercial = UsuarioAreaComercial.objects.filter(usr_codigo=usuario_logado).exists()
    
    # Retorna um valor booleano indicando se o usuário tem vínculo com área comercial
    return JsonResponse({'usuario_comercial': usuario_comercial})



def PasswordRequest(request):
    email = request.data.get('email')
    if not email:
        return Response({'error': 'Email é obrigatório.'}, status=status.HTTP_400_BAD_REQUEST)

    user = get_object_or_404(User, email=email)
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
        
    frontend_url = "http://localhost:5173/redefinir-senha"
    reset_link = f"{frontend_url}/{uid}/{token}"


        # Enviar o email
    send_mail(
        'Redefinição de Senha',
        f'Olá, clique no link para redefinir sua senha: {reset_link}',
        'kauan@webersolucoes.com.br',  # Email remetente deve ser igual ao EMAIL_HOST_USER
        [email],
        fail_silently=False,
    )


    return Response({'message': 'Email de recuperação enviado com sucesso.'}, status=status.HTTP_200_OK)


def PasswordReset(request, uid, token):
    # Aqui estamos recebendo o `uid` e `token` diretamente da URL
    new_password = request.data.get('new_password')

    # Verificar se o parâmetro de nova senha foi passado
    if not new_password:
        return Response({'error': 'Nova senha é obrigatória.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Decodificar o UID e buscar o usuário
        uid = urlsafe_base64_decode(uid).decode('utf-8')
        user = User.objects.get(pk=uid)  # Buscar o usuário pelo ID
    except (User.DoesNotExist, ValueError, TypeError) as e:
        return Response({'error': 'Usuário inválido.'}, status=status.HTTP_400_BAD_REQUEST)

    # Validar o token
    if not default_token_generator.check_token(user, token):
        return Response({'error': 'Token inválido ou expirado.'}, status=status.HTTP_400_BAD_REQUEST)

    # Atualizar a senha
    user.set_password(new_password)
    user.save()

    return Response({'message': 'Senha redefinida com sucesso.'}, status=status.HTTP_200_OK)

