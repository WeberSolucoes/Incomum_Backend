from django.db import models


class Vendedor(models.Model):
    ven_codigo = models.AutoField(primary_key=True)  # Assuming this field is auto-incrementing
    ven_descricao = models.CharField(max_length=60, null=True, blank=True)
    ban_codigo = models.IntegerField(null=True, blank=True)
    ven_agencia = models.CharField(max_length=7, null=True, blank=True)
    ven_contacorrente = models.CharField(max_length=15, null=True, blank=True)
    ven_descricaoweb = models.CharField(max_length=60, null=True, blank=True)
    ven_codigoimportacao = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'vendedor'
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'

    def __str__(self):
        return self.ven_descricao or f'Vendedor {self.ven_codigo}'
