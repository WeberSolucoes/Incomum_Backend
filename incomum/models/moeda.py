from django.db import models

class Moeda(models.Model):
    moe_codigo = models.AutoField(primary_key=True)
    moe_descricao = models.CharField(max_length=50, null=True, blank=True)
    moe_abreviacao = models.CharField(max_length=50, null=True, blank=True)
    moe_simbolo = models.CharField(max_length=30, null=True, blank=True)
    moe_codigogeral = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'moeda'
        # managed = False  # Define como False se a tabela já existir no banco de dados e não quiser que o Django a gerencie
