from django.db import models

class FormaPagamento(models.Model):
    for_codigo = models.AutoField(primary_key=True)
    for_descricao = models.CharField(max_length=50, null=True, blank=True)

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        for field in self._meta.fields:
            if isinstance(field, models.CharField):
                value = getattr(self, field.name)
                if value:
                    setattr(self, field.name, value.upper())
        super(FormaPagamento, self).save(force_insert, force_update, *args, **kwargs)

    class Meta:
        db_table = 'formapagamento'
        # managed = False  # Define como False se a tabela já existir no banco de dados e não quiser que o Django a gerencie
