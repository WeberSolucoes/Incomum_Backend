from django.db import models

class LojaComercial(models.Model):
    loj_codigo = models.AutoField(primary_key=True)
    aco_codigo = models.IntegerField()

    class Meta:
        db_table = 'lojacomercial'
        verbose_name_plural = "LojasComercial"