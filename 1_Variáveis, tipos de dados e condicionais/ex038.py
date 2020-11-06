"""
Escreva um script para classificar um triângulo de acordo com o tamanho dos seus lados. Considere as seguintes
informações:

Triângulo equilátero: todos os lados possuem o mesmo tamanho;

Trângulo escaleno: todos os lados possuem medidas diferentes;

Triângulo isósceles: caracterizado por ter dois lados com o mesmo tamanho.
"""

l1 = int(input('Digite o primeiro lado: '))
l2 = int(input('Digite o segundo lado: '))
l3 = int(input('Digite o terceiro lado: '))

if l1 == l2 == l3:
    print('Triângulo equilátero')
elif (l1 == l2) or (l1 == l3) or (l2 == l3):
    print('Triângulo isósceles')
else:
    print(f'Triângulo escaleno')


