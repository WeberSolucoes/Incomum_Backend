from django.db import models


class Vendedor(models.Model):
    ven_codigo = models.AutoField(primary_key=True)
    ven_descricao = models.CharField(max_length=60, blank=True, null=True)
    ven_endereco = models.CharField(max_length=60, blank=True, null=True)
    ven_numero = models.CharField(max_length=15, blank=True, null=True)
    ven_bairro = models.CharField(max_length=30, blank=True, null=True)
    ven_cep = models.IntegerField(blank=True, null=True)
    cid_codigo = models.IntegerField(blank=True, null=True)
    ven_fone = models.CharField(max_length=17, blank=True, null=True)
    ven_celular = models.CharField(max_length=17, blank=True, null=True)
    ven_email = models.CharField(max_length=50, blank=True, null=True)
    ven_observacao = models.CharField(max_length=170, blank=True, null=True)
    ban_codigo = models.IntegerField(blank=True, null=True)
    ven_agencia = models.CharField(max_length=7, blank=True, null=True)
    ven_contacorrente = models.CharField(max_length=15, blank=True, null=True)
    ven_cpf = models.CharField(max_length=20, blank=True, null=True)
    ven_descricaoauxiliar = models.CharField(max_length=60, blank=True, null=True)
    ven_situacao = models.CharField(max_length=1, blank=True, null=True)
    ven_descricaoweb = models.CharField(max_length=60, blank=True, null=True)
    ven_codigoimportacao = models.IntegerField(blank=True, null=True)
    sve_codigo = models.IntegerField(blank=True, null=True)

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        for field in self._meta.fields:
            if isinstance(field, models.CharField):
                value = getattr(self, field.name)
                if value:
                    setattr(self, field.name, value.upper())
        super(Vendedor, self).save(force_insert, force_update, *args, **kwargs)
    
    class Meta:
        db_table = 'vendedor'
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'

    def __str__(self):
        return self.ven_descricao or f'Vendedor {self.ven_codigo}'
