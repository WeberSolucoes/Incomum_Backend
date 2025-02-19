from django.db import models

class Subgrupo(models.Model):
    sbc_codigo = models.AutoField(primary_key=True)
    sbc_descricao = models.CharField(max_length=50, null=True, blank=True)
    grc_codigo = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'subgrupoconta'
        # managed = False  # Define como False se a tabela já existir no banco de dados e não quiser que o Django a gerencie
