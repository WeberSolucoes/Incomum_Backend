# myapp/middleware.py
from django.http import HttpResponseForbidden

class RestrictIPMiddleware:
    ALLOWED_IPS = ['3.21.123.210']  # Defina o IP permitido aqui

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        if ip not in self.ALLOWED_IPS:
            return HttpResponseForbidden("Access denied.")
        return self.get_response(request)
