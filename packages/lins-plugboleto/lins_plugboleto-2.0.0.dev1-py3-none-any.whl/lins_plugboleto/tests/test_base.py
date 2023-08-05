import unittest
from http import HTTPStatus
from unittest.mock import MagicMock, patch

from requests import Session

from lins_plugboleto.request.base import Base


class MockAuthorize(object):
    def __init__(self, cnpjsh, tokensh, cnpjcedente):
        self.cnpjsh = cnpjsh
        self.tokensh = tokensh
        self.cnpjcedente = cnpjcedente


class TestBase(unittest.TestCase):
    def setUp(self):
        self.authorize = MockAuthorize(
            "cnpjsh_value", "tokensh_value", "cnpjcedente_value"
        )
        self.base = Base(self.authorize)
        self.uri = "http://example.com/"

    @patch.object(Session, "send")
    def test_send_request_no_body(self, mock_send):
        # Configurar resposta simulada
        mock_response = mock_send.return_value
        mock_response.headers = {"Content-Type": "application/json"}
        mock_response.status_code = 200
        mock_response.json.return_value = {"result": "success"}

        # Enviar solicitação
        method = "GET"
        answers, body = self.base.send_request(method, self.uri)

        # Verificar resposta
        self.assertEqual(answers, {"result": "success"})
        self.assertIsNone(body)

        # Verificar chamada de função
        mock_send.assert_called_once()
        call_args = mock_send.call_args[0]
        self.assertEqual(call_args[0].method, method)
        self.assertEqual(call_args[0].url, self.uri)
        self.assertEqual(call_args[0].body, None)
        self.assertEqual(call_args[0].headers["Content-Length"], "0")
        self.assertEqual(call_args[0].headers["cnpj-sh"], self.authorize.cnpjsh)
        self.assertEqual(call_args[0].headers["token-sh"], self.authorize.tokensh)
        self.assertEqual(
            call_args[0].headers["cnpj-cedente"], self.authorize.cnpjcedente
        )

    @patch.object(Session, "send")
    def test_send_request_with_body(self, mock_send):
        # Configurar resposta simulada
        mock_response = mock_send.return_value
        mock_response.headers = {"Content-Type": "application/json"}
        mock_response.status_code = HTTPStatus.OK
        mock_response.json.return_value = {"result": "success"}

        # Dados do corpo da solicitação
        data = {"key": "value"}

        # Enviar solicitação
        method = "POST"
        answers, body = self.base.send_request(method, self.uri, data=data)

        # Verificar resposta
        self.assertEqual(answers, {"result": "success"})
        self.assertEqual(body, data)

        # Verificar chamada de função
        mock_send.assert_called_once()
        call_args = mock_send.call_args[0]
        self.assertEqual(call_args[0].method, method)
        self.assertEqual(call_args[0].url, self.uri)
        self.assertEqual(call_args[0].headers["Content-Type"], "application/json")
        self.assertEqual(call_args[0].headers["cnpj-sh"], self.authorize.cnpjsh)
        self.assertEqual(call_args[0].headers["token-sh"], self.authorize.tokensh)

    @patch.object(Session, "send")
    def test_send_request_raise_exception(self, mock_send):
        # Configurar resposta simulada com código de erro
        mock_response = mock_send.return_value
        mock_response.headers = {
            "User-Agent": "python-requests/2.30.0",
            "Content-Type": "application/json",
        }
        mock_response.status_code = HTTPStatus.BAD_REQUEST
        mock_response.json.return_value = {"error": "Bad request"}

        # Simular exceção retornada
        mock_response.raise_for_status.side_effect = MagicMock(
            side_effect=Exception({"error": "Bad request"})
        )

        # Enviar solicitação
        method = "POST"
        with self.assertRaises(Exception):
            self.base.send_request(method, self.uri)

        # Verificar o código de status mockado
        self.assertEqual(mock_response.status_code, HTTPStatus.BAD_REQUEST)

        # Verificar chamada de função
        mock_send.assert_called_once()
        call_args = mock_send.call_args[0]
        headers = call_args[0].headers
        self.assertEqual(call_args[0].method, method)
        self.assertEqual(call_args[0].url, self.uri)
        self.assertEqual(headers["cnpj-sh"], self.authorize.cnpjsh)
        self.assertEqual(headers["token-sh"], self.authorize.tokensh)
        self.assertEqual(headers["cnpj-cedente"], self.authorize.cnpjcedente)
