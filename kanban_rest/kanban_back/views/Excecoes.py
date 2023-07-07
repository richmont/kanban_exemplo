from rest_framework import exceptions

class ParametroObrigatorio(exceptions.APIException):
    status_code = 400
    default_detail = 'Faltam parâmetros obrigatórios'
    default_code = 'parametro_obrigatorio'

class RecursoNaoEncontrado(exceptions.APIException):
    status_code = 404
    default_detail = "Recurso não encontrado"
    default_code = 'recurso_nao_encontrado'