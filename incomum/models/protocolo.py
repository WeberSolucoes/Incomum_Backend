from django.db import models
from incomum.models.parceiro import Parceiro

class Protocolo(models.Model):
    prt_codigo = models.AutoField(primary_key=True)
    prt_datacadastro = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    prt_datapagamento = models.CharField(max_length=255,null=True, blank=True)
    prt_valor = models.IntegerField(null=True, blank=True)
    usr_codigo = models.IntegerField(null=True, blank=True)
    cta_codigo = models.IntegerField(null=True, blank=True)
    prt_observacao = models.CharField(max_length=255,null=True, blank=True)
    prt_sequencial = models.IntegerField(null=True, blank=True)
    prt_numero = models.IntegerField(null=True, blank=True)
    par_codigo = models.IntegerField(null=True, blank=True)
    prt_numerodocumento = models.IntegerField(null=True, blank=True)
    prt_notafiscal = models.IntegerField(null=True, blank=True)
    spr_codigo = models.IntegerField(null=True, blank=True)
    prt_datavencimento = models.CharField(max_length=255,null=True, blank=True)
    tdu_codigo = models.IntegerField(null=True, blank=True)
    tpa_codigopagamento = models.IntegerField(null=True, blank=True)
    usr_codigopagamento = models.IntegerField(null=True, blank=True)
    age_codigopagamento = models.IntegerField(null=True, blank=True)
    prt_desconto = models.IntegerField(null=True, blank=True)
    prt_juros = models.IntegerField(null=True, blank=True)
    prt_valorbase = models.IntegerField(null=True, blank=True)
    loj_codigo = models.IntegerField(null=True, blank=True)
    moe_codigo = models.IntegerField(null=True, blank=True)
    prt_cambio = models.IntegerField(null=True, blank=True)
    moe_codigopagamento = models.IntegerField(null=True, blank=True)
    prt_cambiopagamento = models.IntegerField(null=True, blank=True)
    prt_previsao = models.IntegerField(null=True, blank=True)
    prt_datacompetencia = models.CharField(max_length=255,null=True, blank=True)
    prt_anomescompetencia = models.CharField(max_length=255,null=True, blank=True)
    prt_transferencia = models.IntegerField(null=True, blank=True)
    prt_numeropagamento = models.IntegerField(null=True, blank=True)
    prt_pagamentoexterno = models.IntegerField(null=True, blank=True)
    prt_custoindireto = models.IntegerField(null=True, blank=True)
    prt_controletransferencia = models.IntegerField(null=True, blank=True)
    prt_restrito = models.IntegerField(null=True, blank=True)
    prt_numerocheque = models.IntegerField(null=True, blank=True)
    age_codigoprogramado = models.IntegerField(null=True, blank=True)
    usr_codigoprogramado = models.IntegerField(null=True, blank=True)
    prt_dataprogramado = models.CharField(max_length=255,null=True, blank=True)
    prt_dataquitacao = models.CharField(max_length=255,null=True, blank=True)
    prt_status = models.IntegerField(null=True, blank=True)
    via_codigo = models.IntegerField(null=True, blank=True)
    vem_codigo = models.IntegerField(null=True, blank=True)
    prt_tipo = models.IntegerField(null=True, blank=True)
    prt_parcela = models.IntegerField(null=True, blank=True)
    prt_parcelatotal = models.IntegerField(null=True, blank=True)
    prt_emprestimo = models.IntegerField(null=True, blank=True)



    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        for field in self._meta.fields:
            if isinstance(field, models.CharField):
                value = getattr(self, field.name)
                if value:
                    setattr(self, field.name, value.upper())
        super(Protocolo, self).save(force_insert, force_update, *args, **kwargs)


    class Meta:
        db_table = 'protocolo'
        #managed = False
