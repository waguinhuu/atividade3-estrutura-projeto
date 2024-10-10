import pytest
from projeto.models.pessoa import Pessoa
from projeto.models.enums.sexo import Sexo

@pytest.fixture
def pessoa_valida():

    pessoa = Pessoa("Marta", 22, Sexo.FEMININO)
    return pessoa


def test_pessoa_nome_valido(pessoa_valida):
    assert pessoa_valida.nome == "Marta"


def test_pessoa_mudar_nome_valido(pessoa_valida):
    pessoa_valida.nome = "Jose"
    assert pessoa_valida.nome == "Jose"


def test_pessoa_idade_valida(pessoa_valida):
    assert pessoa_valida._idade == 22


def test_pessoa_idade_valida(pessoa_valida):
    pessoa_valida._verificar_idade_negativa(-66)
    assert pessoa_valida._idade == 0   