from django.db import models

from incomum.models.agencia import Agencia
from incomum.models.areaComercial import AreaComercial
from incomum.models.loja import Loja
from incomum.models.vendedor import Vendedor

class Relatorio(models.Model):
    fim_codigo = models.AutoField(primary_key=True)
    tur_codigo = models.IntegerField()
    fim_data = models.DateField()
    fim_tipo = models.CharField(max_length=10)
    tur_numerovenda = models.CharField(max_length=20)
    fim_valorliquido = models.FloatField()
    fim_markup = models.FloatField()
    fim_valorinc = models.FloatField()
    fim_valorincajustado = models.FloatField()
    aco_descricao = models.CharField(max_length=20)
    ven_descricao = models.CharField(max_length=40)
    age_descricao = models.CharField(max_length=40)
    fat_valorvendabruta = models.FloatField(null=True)
    loj_codigo = models.IntegerField()
    age_codigo = models.IntegerField()
    aco_codigo = models.IntegerField()



    class Meta:
        db_table = 'faturamentosimplificado'
        verbose_name = 'Faturamento Simplificado'
        verbose_name_plural = 'Faturamentos Simplificados'

