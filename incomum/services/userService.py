
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken  # Importação necessária
from ..serializers.usuarioComercialSerializer import *
from ..models.usuario_areaComercial import UsuarioAreaComercial


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
