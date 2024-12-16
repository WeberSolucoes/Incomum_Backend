# myapp/middleware.py
from django.http import HttpResponseForbidden

class RestrictIPMiddleware:
    ALLOWED_IPS = ['3.21.123.210']  # IP público do seu frontend (IP elástico)

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        # Se a requisição passar por um proxy (Cloudflare, por exemplo), use o X-Forwarded-For
        forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR')
        
        if forwarded_ip:
            ip = forwarded_ip.split(',')[0]

        if ip not in self.ALLOWED_IPS:
            return HttpResponseForbidden("Access denied.")
        return self.get_response(request)



