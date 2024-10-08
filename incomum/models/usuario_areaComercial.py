from django.db import models

class Usuario(models.Model):
    # Campos mínimos que você precisa para evitar referências quebradas
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)

    class Meta:
        managed = False  # Isso impede que Django tente criar ou modificar a tabela

class AreaComercial2(models.Model):
    # Campos mínimos que você precisa para evitar referências quebradas
    name = models.CharField(max_length=255)

    class Meta:
        managed = False  # Isso impede que Django tente criar ou modificar a tabela

class UsuarioAreaComercial(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    area_comercial = models.ForeignKey(AreaComercial2, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('usuario', 'area_comercial')  # Você pode manter isso se necessário
        managed = False  # Isso impede que Django tente criar ou modificar a tabela
