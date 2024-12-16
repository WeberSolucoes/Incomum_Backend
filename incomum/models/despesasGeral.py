from django.db import models

class DespesasGeral(models.Model):
    grc_codigo = models.AutoField(primary_key=True)
    grc_descricao = models.CharField(max_length=50, null=True, blank=True)
    mgr_codigo = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'grupoconta'
        # managed = False  # Define como False se a tabela já existir no banco de dados e não quiser que o Django a gerencie
