from django.db import models

class TipoRegime(models.Model):
    tre_codigo = models.AutoField(primary_key=True)
    tre_descricao = models.CharField(max_length=50, null=True, blank=True)
    tre_descricaoportugues = models.CharField(null=True, blank=True)
    tre_descricaoingles = models.CharField(null=True, blank=True)

    class Meta:
        db_table = 'tiporegime'
        # managed = False  # Define como False se a tabela já existir no banco de dados e não quiser que o Django a gerencie
