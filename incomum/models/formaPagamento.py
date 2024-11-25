from django.db import models

class FormaPagamento(models.Model):
    for_codigo = models.AutoField(primary_key=True)
    for_descricao = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'formapagamento'
        # managed = False  # Define como False se a tabela já existir no banco de dados e não quiser que o Django a gerencie
