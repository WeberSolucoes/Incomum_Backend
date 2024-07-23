from django.db import models

from autenticacaoWeber.models.usuario import Usuario
from .areaComercial import AreaComercial

class UsuarioAreaComercial(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    area_comercial = models.ForeignKey(AreaComercial, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('usuario', 'area_comercial')