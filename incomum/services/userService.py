
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken  # Importação necessária


@csrf_exempt  # Considere usar um token CSRF em vez disso para produção
def login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('loginemail')
            password = data.get('loginsenha')
            if request.user.is_authenticated:
                return JsonResponse({'success': True, 'message': 'Você já está logado!'})

            print(f"Tentando autenticar: email={email}, senha={password}")

            # Tente autenticar o usuário usando email
            usuario = authenticate(request, username=email, password=password)

            if usuario is None:
                print("Autenticação falhou. O usuário pode não existir ou a senha pode estar incorreta.")
                return JsonResponse({'success': False, 'error_message': 'Email ou senha inválidos.'}, status=400)

            print(f"Usuário autenticado: {usuario}")

            if usuario.is_active:
                auth_login(request, usuario)

                # Gerar tokens
                refresh = RefreshToken.for_user(usuario)
                return JsonResponse({
                    'success': True,
                    'access': str(refresh.access_token),  # Retorne o token de acesso
                    'refresh': str(refresh),  # Opcionalmente, você pode retornar o token de atualização
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
