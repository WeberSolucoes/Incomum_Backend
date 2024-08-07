from django.db import models

from incomum.models.agencia import Agencia
from incomum.models.areaComercial import AreaComercial
from incomum.models.loja import Loja
from incomum.models.vendedor import Vendedor

class Relatorio(models.Model):
    fim_codigo = models.AutoField(primary_key=True)  # Assuming this field is auto-incrementing
    tur_codigo = models.IntegerField()
    loj_codigo = models.ForeignKey(Loja, on_delete=models.DO_NOTHING, db_column='loj_codigo', null=True, blank=True)
    ven_codigo = models.ForeignKey(Vendedor, on_delete=models.DO_NOTHING, db_column='ven_codigo', null=True, blank=True)
    age_codigo = models.ForeignKey(Agencia, on_delete=models.DO_NOTHING, db_column='age_codigo', null=True, blank=True)
    fim_data = models.DateField()
    aco_codigo = models.ForeignKey(AreaComercial, on_delete=models.DO_NOTHING, db_column='aco_codigo', null=True, blank=True)
    fim_tipo = models.CharField(max_length=10)
    tur_numerovenda = models.CharField(max_length=20)
    fim_valorliquido = models.FloatField()
    fim_markup = models.FloatField()
    fim_valorinc = models.FloatField()
    fim_valorincajustado = models.FloatField()

    class Meta:
        db_table = 'faturamentosimplificado'
        verbose_name = 'Faturamento Simplificado'
        verbose_name_plural = 'Faturamentos Simplificados'

    def __str__(self):
        return f'Faturamento {self.fim_codigo} - {self.tur_numerovenda}'