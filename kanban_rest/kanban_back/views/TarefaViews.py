from rest_framework import generics, status, exceptions
from kanban_back.models import Quadro, Coluna, Tarefa
from kanban_back.serializers import QuadroSerializer, ColunaSerializer, TarefaSerializer
from kanban_back.views.Excecoes import ParametroObrigatorio, RecursoNaoEncontrado

class TarefaUpdate(generics.UpdateAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer

class TarefaList(generics.ListAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    #queryset = Tarefa.objects.all()
    
    # define que a busca pela coluna está condicionada a presença de um id de quadro
    def get_queryset(self):
        queryset = super().get_queryset()
        #queryset = Tarefa.objects.all()
        coluna_id = self.request.query_params.get('coluna_id', None)
        if coluna_id is not None:
            if queryset.filter(coluna_id=int(coluna_id)).exists():
                return queryset.filter(coluna_id=int(coluna_id))
            else:
                raise RecursoNaoEncontrado(f"coluna id {coluna_id} não existe")
        else:
            raise ParametroObrigatorio('O parâmetro coluna_id é obrigatório.')
