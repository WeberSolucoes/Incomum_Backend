from django.db import models

class AgenciaBancaria(models.Model):
    ban_codigo = models.IntegerField()
    age_codigo = models.AutoField(primary_key=True)
    age_numero = models.CharField(max_length=20, blank=True, null=True)
    age_digito = models.CharField(max_length=20, blank=True, null=True)
    age_agencia = models.CharField(max_length=6, blank=True, null=True)
    age_descricao = models.CharField(max_length=30, blank=True, null=True)
    loj_codigo = models.IntegerField(blank=True, null=True)
    age_situacao = models.CharField(max_length=1, blank=True, null=True)
    age_visualizarelatorio = models.CharField(max_length=1, blank=True, null=True)
    age_visualizaconta = models.CharField(max_length=1, blank=True, null=True)
    age_titularconta = models.CharField(max_length=70, blank=True, null=True)
    age_cnpj = models.CharField(max_length=20, blank=True, null=True)
    age_liberaextrato = models.CharField(max_length=1, blank=True, null=True)
    age_contabil = models.CharField(max_length=20, blank=True, null=True)
    age_liberaunidade = models.CharField(max_length=1, blank=True, null=True)
    age_financiamento = models.CharField(max_length=1, blank=True, null=True)
    age_numeroestabelecimento = models.IntegerField(blank=True, null=True)
    age_liberabaixa = models.CharField(max_length=1, blank=True, null=True)
    age_fechamentomensal = models.CharField(max_length=1, blank=True, null=True)
    age_controlebancario = models.CharField(max_length=1, blank=True, null=True)
    age_cartaoempresa = models.CharField(max_length=1, blank=True, null=True)
    ban_codigobandeira = models.IntegerField(blank=True, null=True)
    age_limite = models.FloatField(blank=True, null=True)
    age_diavencimento = models.IntegerField(blank=True, null=True)
    age_diacorte = models.IntegerField(blank=True, null=True)
    age_tipocartao = models.CharField(max_length=1, blank=True, null=True)
    age_numerocartao = models.CharField(max_length=20, blank=True, null=True)
    age_codigoseguranca = models.CharField(max_length=5, blank=True, null=True)
    age_titular = models.CharField(max_length=60, blank=True, null=True)
    age_validade = models.CharField(max_length=20, blank=True, null=True)
    age_produtos = models.CharField(max_length=20, blank=True, null=True)
    age_prejuizo = models.CharField(max_length=1, blank=True, null=True)
    age_controlekoin = models.CharField(max_length=1, blank=True, null=True)
    age_cartaocredito = models.CharField(max_length=1, blank=True, null=True)
    age_contaexterior = models.IntegerField(blank=True, null=True)
    moe_codigoexterior = models.IntegerField(blank=True, null=True)
    age_cambioexterior = models.FloatField(blank=True, null=True)
    age_saldoexterior = models.FloatField(blank=True, null=True)
    age_pix = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'agenciabancaria'
        verbose_name = 'Agência Bancária'
        verbose_name_plural = 'Agências Bancárias'

    def __str__(self):
        return self.age_descricao
