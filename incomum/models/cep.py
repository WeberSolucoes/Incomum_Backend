from django.db import models
from .loja import Loja

class Cep(models.Model):
    cep_codigo = models.AutoField(primary_key=True)
    cep_logradouro = models.CharField(max_length=50, null=True, blank=True)
    cep_bairro = models.CharField(max_length=50,null=True, blank=True)
    cid_codigo = models.IntegerField(null=True, blank=True)
    cep_numero = models.CharField(max_length=50,null=True, blank=True)
    tlo_codigo = models.IntegerField(null=True, blank=True)

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        for field in self._meta.fields:
            if isinstance(field, models.CharField):
                value = getattr(self, field.name)
                if value:
                    setattr(self, field.name, value.upper())
        super(Cep, self).save(force_insert, force_update, *args, **kwargs)

    class Meta:
        db_table = 'cep'
        # managed = False  # Define como False se a tabela já existir no banco de dados e não quiser que o Django a gerencie
