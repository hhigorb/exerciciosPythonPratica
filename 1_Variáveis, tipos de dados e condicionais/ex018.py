"""
Faça um programa que peça a base e a altura de um retângulo e calcule e mostre na tela a área e o perímetro.
"""

b = int(input('Digite a base do triângulo: '))
h = int(input('Digite a altura do triângulo: '))
area = (b * h) / 2
perimetro = 2 * b + 2 * h

print(f'Base: {b}\n'
      f'Altura: {h}\n'
      f'Área: {area}\n'
      f'Perímetro: {perimetro}')