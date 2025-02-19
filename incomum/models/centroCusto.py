from django.db import models
from .loja import Loja

class CentroCusto(models.Model):
    cta_codigo = models.AutoField(primary_key=True)
    cta_descricao = models.CharField(max_length=50, null=True, blank=True)
    sbc_codigo = models.IntegerField(null=True, blank=True)
    tdu_codigo = models.IntegerField(null=True, blank=True)
    cta_exclusivo = models.IntegerField(null=True, blank=True)
    cta_rateio = models.IntegerField(null=True, blank=True)
    cta_codigocontabil = models.CharField(max_length=20, null=True, blank=True)
    cta_tipo = models.CharField(max_length=20, null=True, blank=True)
    cta_justificativa = models.CharField(max_length=20, null=True, blank=True)

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        for field in self._meta.fields:
            if isinstance(field, models.CharField):
                value = getattr(self, field.name)
                if value:
                    setattr(self, field.name, value.upper())
        super(CentroCusto, self).save(force_insert, force_update, *args, **kwargs)

    class Meta:
        db_table = 'conta'
        # managed = False  # Define como False se a tabela já existir no banco de dados e não quiser que o Django a gerencie
