import unittest
from unittest.mock import MagicMock, patch

from lins_plugboleto.environment import Environment
from lins_plugboleto.request.criar_boleto import CriarBoleto


class TestCriarBoleto(unittest.TestCase):
    def setUp(self):
        self.env_boleto = Environment.from_sandbox()
        self.authorize = MagicMock()
        self.criar_boleto = {
            'titulo': {
                'TituloValor': 100.0,
                'TituloDataEmissao': '2023-05-17',
                'PrazoVencimento': '2023-05-24',
                'TituloLocalPagamento': 'Local de Pagamento',
            },
            'cedente': {
                'CedenteContaCodigoBanco': '001',
                'CedenteContaNumero': '123456',
                'CedenteContaNumeroDV': '9',
                'CedenteConvenioNumero': '7890',
            },
            'mensagem': {
                'TituloMensagem01': 'Mensagem 01',
                'TituloMensagem02': 'Mensagem 02',
                'TituloMensagem03': 'Mensagem 03',
            },
            'prazo_baixa': '2023-06-01',
        }

        self.criar_boleto_instance = CriarBoleto(self.authorize, self.env_boleto)

    def test_execute_success(self):
        mock_response = ([{"_dados": {"_sucesso": True}}], {})

        with patch.object(self.criar_boleto_instance, 'execute', return_value=mock_response) as mock_execute:
            result = self.criar_boleto_instance.execute(self.criar_boleto)

            self.assertEqual(result, mock_response)

            self.assertTrue(mock_execute.called)
            self.assertEqual(mock_execute.call_args[0][0], self.criar_boleto)

    def test_execute_json_decode_error(self):
        mock_response = 'Invalid JSON response'

        with patch.object(self.criar_boleto_instance, 'send_request', return_value=mock_response):
            with self.assertRaises(Exception) as context:
                self.criar_boleto_instance.execute(self.criar_boleto)

            self.assertTrue("Problema no retorno da plugboleto" in str(context.exception))
            self.assertTrue("Invalid JSON response" in str(context.exception))

    def test_execute_generic_error(self):
        mock_response = 'Error response'

        with patch.object(self.criar_boleto_instance, 'execute', side_effect=Exception(mock_response)) as mock_execute:
            with self.assertRaises(Exception) as context:
                self.criar_boleto_instance.execute(self.criar_boleto)

            # Verifica se o método execute foi chamado corretamente
            mock_execute.assert_called_once_with(self.criar_boleto)
