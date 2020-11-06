"""
Determine se uma letra inserida pelo usuário é uma vogal ou consoante. Armazene as vogais em uma lista e
implemente sua solução. Desconsidere a possibilidade de o usuário inserir números ou caracteres especiais.
"""

letra = input('Digite uma letra: ').upper()
vogais = 'AEIOU'

if letra not in vogais:
    print(f'{letra} é uma consoante.')
else:
    print(f'{letra} é uma vogal.')

