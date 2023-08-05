import os
from typing import NamedTuple

from dotenv import load_dotenv


class Environment(NamedTuple):
    """
    Represents the environment configuration for the API.

    Attributes:
        api (str): The URL of the API.
        apidoc (str): The URL of the API documentation.

    Methods:
        from_sandbox(): Create an Environment instance for the sandbox environment.
        from_production(): Create an Environment instance for the production environment.
    """

    api: str
    apidoc: str

    @classmethod
    def from_sandbox(cls) -> "Environment":
        load_dotenv()

        sandbox_api_url = "http://homologacao.plugboleto.com.br/api/v1/"
        sandbox_api_doc_url = (
            "http://apis-sandbox.grupolinsferrao.com.br/api-numerodoc-plugboleto/"
        )

        api = os.getenv("API_URL", sandbox_api_url)
        apidoc = os.getenv("API_DOC_URL", sandbox_api_doc_url)

        return cls(api=api, apidoc=apidoc)

    @classmethod
    def from_production(cls) -> "Environment":
        load_dotenv()

        default_api_url = "https://plugboleto.com.br/api/v1/"
        default_api_doc_url = (
            "http://apis.grupolinsferrao.com.br/api-numerodoc-plugboleto/"
        )

        api = os.getenv("API_URL", default_api_url)
        apidoc = os.getenv("API_DOC_URL", default_api_doc_url)

        return cls(api=api, apidoc=apidoc)
