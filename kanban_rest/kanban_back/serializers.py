from rest_framework import serializers
from .models import Coluna, Quadro, Tarefa

class ColunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coluna
        fields = '__all__'

class QuadroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quadro
        fields = '__all__'

class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = '__all__'