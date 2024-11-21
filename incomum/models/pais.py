from django.db import models

class Pais(models.Model):
    pai_codigo = models.AutoField(primary_key=True)
    pai_descricao = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'pais'
        # managed = False  # Define como False se a tabela já existir no banco de dados e não quiser que o Django a gerencie
