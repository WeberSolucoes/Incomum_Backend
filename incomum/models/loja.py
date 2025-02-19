from django.db import models

class Loja(models.Model):
    loj_codigo = models.AutoField(primary_key=True)
    loj_descricao = models.CharField(max_length=50, null=True, blank=True)
    loj_responsavel = models.CharField(max_length=30, null=True, blank=True)
    loj_email = models.EmailField(max_length=200, null=True, blank=True)
    loj_endereco = models.CharField(max_length=80, null=True, blank=True)
    loj_bairro = models.CharField(max_length=45, null=True, blank=True)
    cep_codigo = models.IntegerField(null=True, blank=True)
    cid_codigo = models.IntegerField(null=True, blank=True)
    loj_fone = models.CharField(max_length=20, null=True, blank=True)
    loj_fax = models.CharField(max_length=20, null=True, blank=True)
    loj_emailloja = models.EmailField(max_length=50, null=True, blank=True)
    loj_emailfinanceiro = models.EmailField(max_length=60, null=True, blank=True)
    loj_textorelatorio = models.CharField(max_length=40, null=True, blank=True)
    loj_cnpj = models.CharField(max_length=20, null=True, blank=True)
    loj_serie = models.IntegerField(null=True, blank=True)
    loj_codigoempresa = models.IntegerField(null=True, blank=True)
    loj_emailbloqueio = models.EmailField(max_length=60, null=True, blank=True)
    loj_situacao = models.IntegerField(null=True, blank=True)
    loj_codigofinanceiro = models.IntegerField(null=True, blank=True)
    aco_codigo = models.ForeignKey('AreaComercial', on_delete=models.DO_NOTHING, db_column='aco_codigo', null=True, blank=True)
    loj_vendacorte = models.IntegerField(null=True, blank=True)
    loj_contrato = models.IntegerField(null=True, blank=True)
    loj_cortevendedor = models.IntegerField(null=True, blank=True)
    nem_codigo = models.IntegerField(null=True, blank=True)

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        for field in self._meta.fields:
            if isinstance(field, models.CharField):
                value = getattr(self, field.name)
                if value:
                    setattr(self, field.name, value.upper())
        super(Loja, self).save(force_insert, force_update, *args, **kwargs)

    class Meta:
        db_table = 'loja'
         # managed = False  # Define como False se a tabela já existir no banco de dados e não quiser que o Django a gerencie
        constraints = [
            models.UniqueConstraint(fields=['loj_codigo'], name='pk_loja')
        ]
        verbose_name_plural = "Lojas"
    def __str__(self):
        return self.loj_descricao
