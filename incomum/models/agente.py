from django.db import models


class Agente(models.Model):
    agt_codigo = models.AutoField(primary_key=True)
    age_codigo = models.CharField(max_length=255)
    agt_descricao = models.CharField(max_length=255)
    agt_cpf = models.IntegerField()
    agt_cep = models.CharField(max_length=255)
    agt_endereco = models.CharField(max_length=255)
    agt_numero = models.IntegerField()
    agt_bairro = models.CharField(max_length=255)
    cid_codigo = models.CharField(max_length=255)
    agt_fone = models.IntegerField()
    agt_celular = models.IntegerField()
    agt_comissao = models.IntegerField()
    agt_email = models.CharField(max_length=255)
    ban_codigo = models.IntegerField()
    agt_agencia = models.IntegerField()
    agt_contacorrente = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'agente'
