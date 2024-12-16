from django.db import models

class Despesas(models.Model):
    mgr_codigo = models.AutoField(primary_key=True)
    mgr_descricao = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'mastergrupoconta'
        # managed = False  # Define como False se a tabela já existir no banco de dados e não quiser que o Django a gerencie
