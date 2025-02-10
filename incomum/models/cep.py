from django.db import models
from .loja import Loja

class Cep(models.Model):
    cep_codigo = models.AutoField(primary_key=True)
    cep_logradouro = models.CharField(max_length=50, null=True, blank=True)
    cep_bairro = models.CharField(max_length=50,null=True, blank=True)
    cid_codigo = models.IntegerField(null=True, blank=True)
    cep_numero = models.CharField(max_length=50,null=True, blank=True)
    tlo_codigo = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'cep'
        # managed = False  # Define como False se a tabela já existir no banco de dados e não quiser que o Django a gerencie
