from django.db import models

class Assinatura(models.Model):
    ass_codigo = models.AutoField(primary_key=True)
    ass_descricao = models.CharField(max_length=50, null=True, blank=True)
    ass_tipoassinatura = models.CharField(null=True, blank=True)
    ass_codigocontabil = models.IntegerField(null=True, blank=True)
    com_codigo = models.IntegerField(null=True, blank=True)
    ass_codigocontabil = models.IntegerField(null=True, blank=True)
    loj_codigobase = models.IntegerField(null=True, blank=True)
    cta_codigobase = models.IntegerField(null=True, blank=True)
    cta_codigosaida = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'assinatura'
        # managed = False  # Define como False se a tabela já existir no banco de dados e não quiser que o Django a gerencie
