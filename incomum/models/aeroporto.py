from django.db import models

class Aeroporto(models.Model):
    aer_codigo = models.AutoField(primary_key=True)
    aer_descricao = models.CharField(max_length=50, null=True, blank=True)
    cid_codigo = models.IntegerField(null=True, blank=True)
    aer_observacao = models.CharField(max_length=50, null=True, blank=True)
    aer_fone = models.CharField(max_length=50, null=True, blank=True)
    aer_email = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'aeroporto'
        # managed = False  # Define como False se a tabela já existir no banco de dados e não quiser que o Django a gerencie
