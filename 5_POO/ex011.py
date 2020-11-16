"""
Crie uma classe Pessoa com os atributos nome, idade e telefone (privado) e um método resumo, para mostrar na
tela todos os atributos. Em seguida crie uma classe PessoaUniversidade que herde todos os métodos e atributos
da classe Pessoa, mas que implemente o atributo universidade e sobrescreva o método resumo.
"""


class Pessoa:
    def __init__(self, nome, idade, telefone):
        self.nome = nome
        self.idade = idade
        self.__telefone = telefone

    @property
    def resumo(self):
        return self.__dict__


class PessoaUniversidade(Pessoa):
    def __init__(self, nome, idade, telefone, universidade):
        super().__init__(nome, idade, telefone)
        self.universidade = universidade

    @property
    def resumo(self):
        return self.__dict__


pessoa1 = PessoaUniversidade('Higor', 20, 'xxxxxxxxxx', 'AM')
print(pessoa1.resumo)

pessoa2 = Pessoa('Marcos', 30, 'xxxxxxxxx')
print(pessoa2.resumo)