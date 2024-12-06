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
    usr_codigo = models.IntegerField(primary_key=True)
    aco_codigo = models.IntegerField()

    class Meta:
        db_table = 'usuariocomercial'
        managed = False  # Isso impede que Django tente criar ou modificar a tabela
