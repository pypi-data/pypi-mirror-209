import os
from distutils.core import setup

from setuptools import find_packages


def get_version():
    return open("version.txt", "r").read().strip()


# Obter o caminho do diretório atual
here = os.path.abspath(os.path.dirname(__file__))

# Modificar o caminho do arquivo 'requirements.txt'
with open(os.path.join(here, "requirements.txt")) as f:
    requirements = f.read().splitlines()


setup(
    name="lins_plugboleto",
    description="Pacote de consumo da Plug Boleto",
    author="Vinicius Languer",
    author_email="vinicius@lojaspompeia.com.br",
    long_description="🗂 Simple Python Package",
    license="MIT",
    packages=find_packages(),
    url="https://bitbucket.org/grupolinsferrao/pypck-lins-plugboleto/",
    version=get_version(),
    keywords=["plugboleto", "lojaspompeia" "python"],
    zip_safe=False,
    install_requires=requirements,
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
