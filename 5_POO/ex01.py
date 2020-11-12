"""
Crie uma classe Pessoa com os seguintes atributos: nome, sobrenome e idade.
"""


class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade


pessoa1 = Pessoa('higor', 'henrique', 20)
print(pessoa1.nome)