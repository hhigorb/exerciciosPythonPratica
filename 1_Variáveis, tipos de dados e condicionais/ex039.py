"""
Implemente uma calculadora simples com as operações aritméticas básicas. O usuário deverá especificar a
operação desejada (+,-,*,/) e seguidamente inserir dois valores. Caso, o usuário escolha divisão e insira o
valor do denominar 0 mostre uma mensagem personalizada. Para os demais casos, mostre na tela o resultado
da operação desejada.
"""

v1 = int(input('Digite um número: '))
v2 = int(input('Digite outro número: '))
operacao = input('Escolha a operação desejada: [+  -  *  /]: ')
if operacao in '+-*/':
    if operacao == '+':
        print(f'{v1} + {v2} = {v1 + v2}')
    elif operacao == '-':
        print(f'{v1} - {v2} = {v1 - v2}')
    elif operacao == '*':
        print(f'{v1} * {v2} = {v1 * v2}')
    elif operacao == '/':
        if v2 == 0:
            print('Não é possível dividir por 0.')
        else:
            print(f'{v1} / {v2} = {v1 / v2}')
else:
    print('Operação inválida!')


