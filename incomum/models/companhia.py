from django.db import models

class Companhia(models.Model):
    com_codigo = models.AutoField(primary_key=True)
    com_descricao = models.CharField(max_length=50, null=True, blank=True)
    com_divisao = models.CharField(null=True, blank=True)
    com_parcelaminima = models.IntegerField(null=True, blank=True)
    com_sequencial = models.IntegerField(null=True, blank=True)
    com_sigla = models.CharField(null=True, blank=True)
    par_codigo = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'companhia'
        # managed = False  # Define como False se a tabela já existir no banco de dados e não quiser que o Django a gerencie
