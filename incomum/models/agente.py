from django.db import models


class Agente(models.Model):
    agt_codigo = models.AutoField(primary_key=True)
    age_codigo = models.CharField(null=True, blank=True,max_length=255)
    agt_descricao = models.CharField(null=True, blank=True,max_length=255)
    agt_cpf = models.IntegerField(null=True, blank=True)
    agt_cep = models.CharField(null=True, blank=True,max_length=255)
    agt_endereco = models.CharField(null=True, blank=True,max_length=255)
    agt_numero = models.IntegerField(null=True, blank=True)
    agt_bairro = models.CharField(null=True, blank=True,max_length=255)
    cid_codigo = models.CharField(null=True, blank=True,max_length=255)
    agt_fone = models.IntegerField(null=True, blank=True)
    agt_celular = models.IntegerField(null=True, blank=True)
    agt_comissao = models.IntegerField(null=True, blank=True)
    agt_email = models.CharField(null=True, blank=True,max_length=255)
    ban_codigo = models.IntegerField(null=True, blank=True)
    agt_agencia = models.IntegerField(null=True, blank=True)
    agt_contacorrente = models.IntegerField(null=True, blank=True)

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        for field in self._meta.fields:
            if isinstance(field, models.CharField):
                value = getattr(self, field.name)
                if value:
                    setattr(self, field.name, value.upper())
        super(Agente, self).save(force_insert, force_update, *args, **kwargs)

    class Meta:
        managed = False
        db_table = 'agente'
