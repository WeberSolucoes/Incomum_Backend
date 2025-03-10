from django.db import models
from .loja import Loja

class AreaComercial(models.Model):
    aco_codigo = models.AutoField(primary_key=True)
    aco_descricao = models.CharField(max_length=50, null=True, blank=True)
    aco_datacadastro = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    aco_situacao = models.IntegerField(null=True, blank=True)
    aco_rateio = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'areacomercial'
        # managed = False  # Define como False se a tabela já existir no banco de dados e não quiser que o Django a gerencie
