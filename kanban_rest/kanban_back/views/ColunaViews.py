from rest_framework import generics, status, exceptions
from rest_framework.response import Response
from kanban_back.models import Quadro, Coluna, Tarefa
from kanban_back.serializers import QuadroSerializer, ColunaSerializer, TarefaSerializer
from kanban_back.views.Excecoes import ParametroObrigatorio, RecursoNaoEncontrado


# Atualizar
class QuadroUpdate(generics.UpdateAPIView):
    queryset = Quadro.objects.all()
    serializer_class = QuadroSerializer

class ColunaUpdate(generics.UpdateAPIView):
    queryset = Coluna.objects.all()
    serializer_class = ColunaSerializer



# Listar
class QuadroList(generics.ListAPIView):
    queryset = Quadro.objects.all()
    serializer_class = QuadroSerializer

class ColunaList(generics.ListAPIView):
    #queryset = Coluna.objects.all()
    serializer_class = ColunaSerializer
    # define que a busca pela coluna está condicionada a presença de um id de quadro
    def get_queryset(self):
        #queryset = super().get_queryset()
        queryset = Coluna.objects.all()
        quadro_id = self.request.query_params.get('quadro_id', None)
        if quadro_id is not None:
            if queryset.filter(quadro_id=int(quadro_id)).exists():
                return queryset.filter(quadro_id=int(quadro_id))
            else:
                raise RecursoNaoEncontrado(f"Quadro id {quadro_id} não existe")
        else:
            raise ParametroObrigatorio('O parâmetro quadro_id é obrigatório.')

# Deletar
class QuadroDelete(generics.DestroyAPIView):
    queryset = Quadro.objects.all()
    serializer_class = QuadroSerializer

class ColunaDelete(generics.DestroyAPIView):
    queryset = Coluna.objects.all()
    serializer_class = ColunaSerializer

class TarefaDelete(generics.DestroyAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer