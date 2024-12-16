# myapp/middleware.py
from django.http import HttpResponseForbidden

class RestrictIPMiddleware:
    ALLOWED_IPS = ['3.21.123.210', '172.31.28.99']  # Adicione o IP público e privado

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Verificar o IP da requisição
        ip = request.META.get('REMOTE_ADDR')
        forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR')
        
        # Caso esteja atrás de um proxy, considere o X-Forwarded-For
        if forwarded_ip:
            ip = forwarded_ip.split(',')[0]

        if ip not in self.ALLOWED_IPS:
            return HttpResponseForbidden("Access denied.")
        return self.get_response(request)


