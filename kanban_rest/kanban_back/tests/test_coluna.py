from django.test import TestCase
from kanban_back.models import Coluna, Quadro

class ColunaModelTest(TestCase):
    #databases = {'default', 'test'}
    database_alias = 'test'
    @classmethod
    def setUpTestData(cls):
        q = Quadro.objects.create(nome='Meu quadro')
        Coluna.objects.create(nome='Minha coluna', quadro=q)

    def test_nome_label(self):
        coluna = Coluna.objects.get(id=1)
        field_label = coluna._meta.get_field('nome').verbose_name
        self.assertEquals(field_label, 'nome')

    def test_nome_max_length(self):
        coluna = Coluna.objects.get(id=1)
        max_length = coluna._meta.get_field('nome').max_length
        self.assertEquals(max_length, 50)

    def test_object_name_is_nome(self):
        coluna = Coluna.objects.get(id=1)
        expected_object_name = f'{coluna.nome}'
        self.assertEquals(expected_object_name, str(coluna.nome))
