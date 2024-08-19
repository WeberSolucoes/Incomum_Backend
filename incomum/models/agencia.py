from django.db import models

class Agencia(models.Model):
    age_codigo = models.AutoField(primary_key=True)
    age_descricao = models.CharField(max_length=70)
    age_endereco = models.CharField(max_length=60, null=True, blank=True)
    age_numero = models.CharField(max_length=20, null=True, blank=True)
    age_bairro = models.CharField(max_length=35, null=True, blank=True)
    age_cep = models.IntegerField(null=True, blank=True)
    cid_codigo = models.IntegerField(null=True, blank=True)
    age_fone = models.CharField(max_length=20, null=True, blank=True)
    age_celular = models.CharField(max_length=20, null=True, blank=True)
    age_observacao = models.CharField(max_length=180, null=True, blank=True)
    age_dataatualizacao = models.DateTimeField(null=True, blank=True)
    age_datacadastro = models.DateTimeField(null=True, blank=True)
    ban_codigo = models.IntegerField(null=True, blank=True)
    age_agencia = models.CharField(max_length=5, null=True, blank=True)
    age_contacorrente = models.CharField(max_length=15, null=True, blank=True)
    age_complementar = models.CharField(max_length=1, null=True, blank=True)
    age_codigocontabil = models.IntegerField(null=True, blank=True)
    age_cnpj = models.CharField(max_length=20, null=True, blank=True)
    age_situacao = models.CharField(max_length=1, null=True, blank=True)
    age_comissao = models.FloatField(null=True, blank=True)
    age_over = models.FloatField(null=True, blank=True)
    par_codigo = models.IntegerField(null=True, blank=True)
    age_imagem = models.BinaryField(null=True, blank=True)
    age_descricaosite = models.CharField(max_length=70, null=True, blank=True)
    age_verificar = models.CharField(max_length=1, null=True, blank=True)
    age_inscricaomunicipal = models.CharField(max_length=20, null=True, blank=True)
    age_markup = models.FloatField(null=True, blank=True)
    aco_codigo = models.ForeignKey('AreaComercial', on_delete=models.DO_NOTHING, db_column='aco_codigo', null=True, blank=True)
    age_markupliberado = models.FloatField(null=True, blank=True)
    age_codigoprincipal = models.IntegerField(null=True, blank=True)
    age_codigoimportacao = models.IntegerField(null=True, blank=True)
    age_razaosocial = models.CharField(max_length=80, null=True, blank=True)

    class Meta:
        db_table = 'agencia'
        verbose_name = 'Agencia'
        verbose_name_plural = 'Agencias'

    def __str__(self):
        return self.age_descricao or str(self.age_codigo)
