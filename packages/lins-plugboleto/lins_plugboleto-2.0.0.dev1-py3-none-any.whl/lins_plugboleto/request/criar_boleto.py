import json

from .base import Base


class CriarBoleto(Base):
    def __init__(self, authorize, environment):
        super(CriarBoleto, self).__init__(authorize)

        self.environment = environment

    def execute(self, criar_boleto):
        response = None
        uri = f"{self.environment.api}boletos/lote"

        try:
            response = self.send_request("POST", uri, criar_boleto)
            body = response[1]
            body = json.loads(json.dumps(body))
            sucesso = response[0]["_dados"]["_sucesso"]
            if sucesso:
                criar_boleto.update_return(response[0], body)
        except json.JSONDecodeError as error:
            raise Exception(
                f"Problema no retorno da plugboleto: {error} - Json inválido: {response}"
            ) from error
        except Exception as error:
            raise Exception(
                f"Problema no retorno da plugboleto: {error} - Response: {response}"
            ) from error

        return response
