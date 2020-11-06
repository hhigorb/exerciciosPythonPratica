"""
Escreva um programa que receba o nome, sobrenome e idade do usuário e apresente a seguinte mensagem na tela:

"Seja bem-vindo [nome] [sobrenome]."

"Você possui [idade] anos de idade."
"""

nome = input('Nome: ').title()
sobrenome = input('Sobrenome: ').title()
idade = int(input('Idade: '))

print(f'Seja bem vindo {nome} {sobrenome}\n'
      f'Você possui {idade} anos de idade!')
