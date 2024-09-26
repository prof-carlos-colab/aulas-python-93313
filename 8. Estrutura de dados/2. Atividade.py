import os
from dataclasses import dataclass

os.system("cls || clear")

# Estrutura de dados.
@dataclass
class Cliente:
    nome: str
    sobrenome: str
    idade: int
    peso: float
    altura: float

QUANTIDADE_ALUNOS = 4


# Salvar em um arquivo chamado: carteira_de_clientes.txt

# Fazer leitura de dados do arquivo carteira_de_clientes.txt e mostre no terminal.