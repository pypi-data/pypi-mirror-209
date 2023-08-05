import unittest
from unittest import mock

from lins_plugboleto.request.busca_boleto import BuscaBoleto


class TestBuscaBoleto(unittest.TestCase):
    def test_execute_returns_expected_result(self):
        # Mock da classe Environment
        environment_mock = mock.MagicMock()
        environment_mock.api = "https://plugboleto.com.br/api/v1/"

        # Criar uma instância de BuscaBoleto
        busca_boleto = BuscaBoleto(authorize="token", environment=environment_mock)

        # Substituir o atributo 'send_request' da instância por um mock
        busca_boleto.send_request = mock.MagicMock(return_value="resultado esperado")

        # Chamar o método execute
        result = busca_boleto.execute(id_integracao="123")

        # Verificar se o mock do método 'send_request' foi chamado corretamente
        busca_boleto.send_request.assert_called_once_with(
            "GET", "https://plugboleto.com.br/api/v1/boletos?IdIntegracao=123"
        )

        # Verificar se o resultado retornado é o esperado
        self.assertEqual(result, "resultado esperado")
