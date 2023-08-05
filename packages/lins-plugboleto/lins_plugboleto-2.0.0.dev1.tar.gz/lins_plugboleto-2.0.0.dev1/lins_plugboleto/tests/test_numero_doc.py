import unittest
from unittest import mock

from lins_plugboleto.environment import Environment
from lins_plugboleto.request.numero_doc import NumeroDoc


class TestNumeroDoc(unittest.TestCase):
    def setUp(self) -> None:
        self.env_boleto = Environment.from_sandbox()
        self.expected_uri = f"{self.env_boleto.apidoc}numerodoc"
        return super().setUp()

    def test_execute_success(self):
        # Criar uma instância de NumeroDoc
        numero_doc = NumeroDoc(authorize="token", environment=self.env_boleto)

        # Mock do método 'request_numerodoc'
        numero_doc.request_numerodoc = mock.MagicMock(return_value="resultado esperado")

        # Chamar o método execute
        result = numero_doc.execute()

        # Verificar se o mock do método 'request_numerodoc' foi chamado corretamente
        numero_doc.request_numerodoc.assert_called_once_with("POST", self.expected_uri)

        # Verificar se o resultado retornado é o esperado
        self.assertEqual(result, "resultado esperado")
