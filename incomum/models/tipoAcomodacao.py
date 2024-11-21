from django.db import models

class TipoAcomodacao(models.Model):
    tac_codigo = models.AutoField(primary_key=True)
    tac_descricao = models.CharField(max_length=50, null=True, blank=True)
    tac_descricaoportugues = models.CharField(null=True, blank=True)
    tac_qtde = models.IntegerField(null=True, blank=True)
    tac_descricaoingles = models.CharField(null=True, blank=True)

    class Meta:
        db_table = 'tipoacomodacao'
        # managed = False  # Define como False se a tabela já existir no banco de dados e não quiser que o Django a gerencie
