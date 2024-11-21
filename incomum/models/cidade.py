from django.db import models

class Cidade(models.Model):
    cid_codigo = models.AutoField(primary_key=True)
    cid_descricao = models.CharField(max_length=50, null=True, blank=True)
    cid_estado = models.CharField(max_length=50, null=True, blank=True)
    reg_codigo = models.IntegerField(null=True, blank=True)
    cid_pais = models.CharField(max_length=30, null=True, blank=True)
    cid_sigla = models.CharField(max_length=10, null=True, blank=True)
    pai_codigo = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'cidade'
        # managed = False  # Define como False se a tabela já existir no banco de dados e não quiser que o Django a gerencie
