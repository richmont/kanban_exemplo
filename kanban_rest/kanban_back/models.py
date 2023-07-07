from django.db import models

# Create your models here.
class Quadro(models.Model):
    nome = models.CharField(max_length=50)
    #class Meta:
    #    app_label = 'kanban_back'

class Coluna(models.Model):
    nome = models.CharField(max_length=50)
    quadro = models.ForeignKey(Quadro, on_delete=models.CASCADE)
    #class Meta:
    #    app_label = 'kanban_back'

class Tarefa(models.Model):
    descricao = models.CharField(max_length=500)
    coluna = models.ForeignKey(Coluna, on_delete=models.CASCADE)
    #class Meta:
    #    app_label = 'kanban_back'