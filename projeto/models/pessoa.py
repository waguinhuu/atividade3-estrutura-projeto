from projeto.models.enums.sexo import Sexo

class Pessoa:

    def __init__(self, nome: str, idade: int, sexo: Sexo) -> None:
        self.nome = nome
        self._idade = self.set_idade(idade)
        self._sexo = sexo
    
    def set_idade(self, idade):
        if not self._verificar_idade_negativa(idade):
            self._idade = idade

    def _verificar_idade_negativa(self, idade) -> int:
        if idade < 0:
        
            self._idade = 0
            return self._idade
    
    def __str__(self) -> str:
        return (
            f"Nome: {self._nome}"
            f"\nIdade: {self._idade}"
            f"\nSexo: {self._sexo.value}"
        )