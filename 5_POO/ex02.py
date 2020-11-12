"""
Acrescente a classe Pessoa um método para mostrar os dados de uma pessoa. Crie um objeto do tipo Pessoa para
testar suas propriedades e métodos.
"""


class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def mostra_dados(self):
        return f'Seu nome é: {self.nome} {self.sobrenome} e a idade é: {self.idade}'


pessoa1 = Pessoa('Higor', 'Henrique', 20)
print(pessoa1.mostra_dados())