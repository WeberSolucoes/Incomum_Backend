from django.db import models

class Classe(models.Model):
    cla_codigo = models.AutoField(primary_key=True)
    cla_descricao = models.CharField(max_length=50, null=True, blank=True)
    cla_observacao = models.TextField(max_length=120, null=True, blank=True)

    class Meta:
        db_table = 'classe'
        # managed = False  # Define como False se a tabela já existir no banco de dados e não quiser que o Django a gerencie
