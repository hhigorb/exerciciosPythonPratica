"""
Modifique o programa anterior e permita que o usuário especifique o ano e o mês a serem mostrados na tela.
"""

import calendar

mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))

print(calendar.month(ano, mes))