from django.db import models


class Tarefa(models.Model):
    nome = models.CharField(max_length=200)
    concluida = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = 'Tarefas'
