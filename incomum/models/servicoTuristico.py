from django.db import models

class ServicoTuristico(models.Model):
    ser_codigo = models.AutoField(primary_key=True)
    ser_descricao = models.CharField(max_length=50, null=True, blank=True)
    cid_codigo = models.IntegerField(null=True, blank=True)
    ser_livre = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'servico'
        # managed = False  # Define como False se a tabela já existir no banco de dados e não quiser que o Django a gerencie
