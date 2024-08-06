from django.db import models

from autenticacaoWeber.models.usuario import Usuario

class Vendedor(models.Model):
    ven_codigo = models.AutoField(primary_key=True)  # Assuming this field is auto-incrementing
    ban_codigo = models.IntegerField(null=True, blank=True)
    ven_agencia = models.CharField(max_length=7, null=True, blank=True)
    ven_contacorrente = models.CharField(max_length=15, null=True, blank=True)
    ven_descricaoweb1= models.CharField(max_length=60, null=True, blank=True)
    ven_descricaoweb2 = models.CharField(max_length=60, null=True, blank=True)
    ven_codigoimportacao = models.IntegerField(null=True, blank=True)
    usr_codigo = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, db_column='usr_codigo', null=True, blank=True)
    class Meta:
        db_table = 'vendedor'
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'

    def __str__(self):
        return self.ven_descricao or f'Vendedor {self.ven_codigo}'
