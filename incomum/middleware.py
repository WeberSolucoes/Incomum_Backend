from django.http import HttpResponseForbidden

class RestrictIPMiddleware:
    ALLOWED_IPS = ['3.21.123.210', '172.31.28.99']  # Adicione os IPs públicos e privados permitidos aqui

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        # Se a requisição estiver atrás de um proxy, verifique o cabeçalho 'X-Forwarded-For'
        forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR')
        if forwarded_ip:
            ip = forwarded_ip.split(',')[0]  # Pega o primeiro IP da lista no cabeçalho

        if ip not in self.ALLOWED_IPS:
            return HttpResponseForbidden("Access denied.")
        return self.get_response(request)

