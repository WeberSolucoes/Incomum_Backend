
from django.db import models
from incomum.models.parceiro import Parceiro

class ParceiroContato(models.Model):
    pco_codigo = models.AutoField(primary_key=True)
    par_codigo = models.IntegerField()
    pco_descricao = models.CharField(max_length=255,null=True, blank=True)
    pco_observacao = models.CharField(max_length=255,null=True, blank=True)
    pco_fone = models.CharField(max_length=255,null=True, blank=True)
    pco_celular = models.CharField(max_length=255,null=True, blank=True)
    pco_datacadastro = models.CharField(max_length=255,null=True, blank=True)
    tco_codigo = models.IntegerField(null=True, blank=True)

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        for field in self._meta.fields:
            if isinstance(field, models.CharField):
                value = getattr(self, field.name)
                if value:
                    setattr(self, field.name, value.upper())
        super(ParceiroContato, self).save(force_insert, force_update, *args, **kwargs)


    class Meta:
        db_table = 'parceirocontato'
        #managed = False
