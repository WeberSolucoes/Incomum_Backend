from django.db import models

from incomum.models.agencia import Agencia
from incomum.models.areaComercial import AreaComercial
from incomum.models.loja import Loja
from incomum.models.vendedor import Vendedor

class Relatorio(models.Model):
    fim_codigo = models.AutoField(primary_key=True)  # Assuming this field is auto-incrementing
    tur_codigo = models.IntegerField()
    fim_data = models.DateField()
    fim_tipo = models.CharField(max_length=10)
    tur_numerovenda = models.CharField(max_length=20)
    fim_valorliquido = models.FloatField()
    fim_markup = models.FloatField()
    fim_valorinc = models.FloatField()
    fim_valorincajustado = models.FloatField()
    aco_codigo = models.IntegerField()
    loj_codigo = models.IntegerField()
    age_codigo = models.IntegerField()
    ven_codigo = models.IntegerField()



    class Meta:
        db_table = 'faturamentosimplificado'
        verbose_name = 'Faturamento Simplificado'
        verbose_name_plural = 'Faturamentos Simplificados'

    def __str__(self):
        return f'Faturamento {self.fim_codigo} - {self.tur_numerovenda}'
