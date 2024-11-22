from django.db import models

class SituacaoTuristico(models.Model):
    stu_codigo = models.AutoField(primary_key=True)
    stu_descricao = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'situacaoturistico'
        # managed = False  # Define como False se a tabela já existir no banco de dados e não quiser que o Django a gerencie
