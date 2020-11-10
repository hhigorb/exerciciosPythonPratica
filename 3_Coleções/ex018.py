"""
18.1 Crie um script para iterar no dicionário abaixo e mostrar na tela todas as suas chaves, uma a uma.

produto1={
    'nome':'produto1',
    'tipo':'categoriaA',
    'valor':'50.5',
    'fornecedor':'ABCD',
}

Output:

nome
tipo
valor
fornecedor

18.2 Crie um script para iterar no dicionário produto1 e mostrar na tela todos os seus valores, um a um.

Output:


produto1
categoriaA
50.5
ABCD

18.3 Crie um script para iterar no dicionário produto1 e mostrar chave,valor na tela.

Output:


nome produto1
tipo categoriaA
valor 50.5
fornecedor ABCD
Dica: utilize o método items().
"""

# 18.1:

produto1 = {
    'nome': 'produto1',
    'tipo': 'categoriaA',
    'valor': '50.5',
    'fornecedor': 'ABCD',
}

for chave in produto1.keys():
    print(chave)

# 18.2:

for valor in produto1.values():
    print(valor)

# 18.3:

for chave, valor in produto1.items():
    print(chave, valor)
