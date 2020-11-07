"""
Elabore um programa para imprimir a sequência de Fibonacci até o n-ésimo termo definido pelo usuário.
Certifique que o usuário digite um número inteiro positivo.

0,1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584,...
"""

n = int(input('Digite o número limite: '))
anterior = 0
proximo = 0

for i in range(0, n+1):
    print(proximo)
    proximo = proximo + anterior
    anterior = proximo - anterior
    if proximo == 0:
        proximo = proximo + 1


