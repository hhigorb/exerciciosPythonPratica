"""
Crie uma classe Produto com as seguintes características:

Atributos:

Nome;

Estoque;

Descrição;

Preço.

Métodos:

Mostrar nome;

Mostrar estoque;

Mostrar preço;

Mudar nome;

Mudar estoque;

Mudar descrição;

Mudar preço;

Sumário (mostrar na tela todos os atributos de instância).
"""


class Produto:
    def __init__(self, nome, estoque, descricao, preco):
        self.nome = nome
        self.estoque = estoque
        self.descricao = descricao
        self.preco = preco

    def mostrar_nome(self):
        return self.nome

    def mostrar_estoque(self):
        return self.estoque

    def mostrar_preco(self):
        return self.preco

    def mudar_nome(self, novo_nome):
        self.nome = novo_nome

    def mudar_estoque(self, novo_estoque):
        self.estoque = novo_estoque

    def mudar_descricao(self, nova_desc):
        self.descricao = nova_desc

    def mudar_preco(self, novo_preco):
        self.preco = novo_preco

    def sumario(self):
        print('Sumário do produto')
        print(f'Produto: {self.nome}')
        print(f'Estoque: {self.estoque}')
        print(f'Descrição: {self.descricao}')
        print(f'Preço: {self.preco}')


p1 = Produto('PS4', 100, 'Videogame Sony', 2300.00)
print(p1.mostrar_nome())
print(p1.mostrar_estoque())
print(p1.mostrar_preco())

p1.mudar_nome('Xbox One')
p1.mudar_estoque(200)
p1.mudar_preco(1500)
p1.mudar_descricao('Videogame Microsoft')

p1.sumario()