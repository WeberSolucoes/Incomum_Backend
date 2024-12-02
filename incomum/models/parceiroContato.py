
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


    class Meta:
        db_table = 'parceirocontato'
        #managed = False
