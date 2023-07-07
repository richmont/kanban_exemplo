from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Quadro, Coluna, Tarefa


class ListarQuadros(APIView):

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        quadros = Quadro.objects.all()
        return Response(quadros)

class ListarColunas(APIView):

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        colunas = Coluna.objects.all()
        return Response(colunas)

class ListarTarefas(APIView):

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        tarefas = Tarefa.objects.all()
        return Response(tarefas)