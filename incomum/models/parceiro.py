
from django.db import models


class Parceiro(models.Model):
    par_codigo = models.AutoField(primary_key=True)
    par_descricao = models.CharField(max_length=255,null=True, blank=True)
    par_tipopessoa = models.CharField(max_length=255,null=True, blank=True)
    par_cnpjcpf = models.CharField(max_length=255,null=True, blank=True)
    par_rgie = models.CharField(max_length=255,null=True, blank=True)
    par_datanascfund = models.CharField(max_length=255,null=True, blank=True)
    par_fone1 = models.CharField(max_length=255,null=True, blank=True)
    par_fone2 = models.CharField(max_length=255,null=True, blank=True)
    par_celular = models.CharField(max_length=255,null=True, blank=True)
    par_fax = models.CharField(max_length=255,null=True, blank=True)
    par_endereco = models.CharField(max_length=255,null=True, blank=True)
    par_bairro = models.CharField(max_length=255,null=True, blank=True)
    par_numero = models.CharField(max_length=255,null=True, blank=True)
    par_complemento = models.CharField(max_length=255,null=True, blank=True)
    cid_codigo = models.IntegerField(null=True, blank=True)
    par_cep = models.CharField(max_length=255,null=True, blank=True)
    par_obs = models.CharField(max_length=255,null=True, blank=True)
    par_email = models.CharField(max_length=255,null=True, blank=True)
    par_site = models.CharField(max_length=255,null=True, blank=True)
    par_datacadastro = models.CharField(max_length=255,null=True, blank=True)
    par_dataatualizacao = models.CharField(max_length=255,null=True, blank=True)
    spa_codigo = models.IntegerField(null=True, blank=True)
    tcr_codigo = models.IntegerField(null=True, blank=True)
    par_atualiza = models.CharField(max_length=255,null=True, blank=True)
    par_pagamentoentrada = models.IntegerField(null=True, blank=True)
    par_pagamentosaida = models.IntegerField(null=True, blank=True)
    cta_codigo = models.IntegerField(null=True, blank=True)
    par_razaosocial = models.CharField(max_length=255,null=True, blank=True)
    par_whatsapp = models.CharField(max_length=255,null=True, blank=True)
    par_codigoimportacao = models.IntegerField(null=True, blank=True)


    class Meta:
        db_table = 'parceiro'
        #managed = False
