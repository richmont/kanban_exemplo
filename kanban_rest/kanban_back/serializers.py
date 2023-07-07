from rest_framework import serializers
from .models import Coluna, Quadro, Tarefa

class QuadroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quadro
        fields = '__all__'

class ColunaSerializer(serializers.ModelSerializer):
    quadro_nome = serializers.ReadOnlyField(source='quadro.id')
    class Meta:
        model = Coluna
        fields = '__all__'

class TarefaSerializer(serializers.ModelSerializer):
    coluna_nome = serializers.ReadOnlyField(source='coluna.id')
    class Meta:
        model = Tarefa
        fields = '__all__'