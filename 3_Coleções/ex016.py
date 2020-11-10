"""
Considere a tupla1 e responda as seguintes questões:

tupla1=('A','B','A','Z','Z','X','A','E','K','G','H')

a) mostre na tela o tamanho desta tupla;

b) ordene a tupla e mostre o resultado na tela;

c) mostre na tela o número de ocorrências da string 'A';

d) mostre na tela o número de ocorrências da string 'B';

e) mostre na tela o índice da string 'X';

f) mostre na tela o último elemento da tupla1.
"""

tupla = ('A', 'B', 'A', 'Z', 'Z', 'X', 'A', 'E', 'K', 'G', 'H')

print(len(tupla))
print(sorted(tupla))
print(tupla.count('A'))
print(tupla.count('B'))
print(tupla.index('X'))
print(tupla[-1])


